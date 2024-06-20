"""账户交易操作类"""

import polars as pl
import logging
import json
from pathlib import Path
from typing import Dict, Union, Optional, Any, Iterator
from collections import defaultdict
from pydantic import Field
from vxutils.datamodel.core import VXDataModel
from vxutils import to_json


class VXSubPortfolio(VXDataModel):
    """子组合信息"""

    subportfolio_id: str = Field(..., description="子组合名称")
    strategy: str = Field(..., description="子组合策略")
    ratio: float = Field(..., description="子组合占比")
    weights: Dict[str, float] = Field(..., description="权重信息")

    def rebalance(
        self, weights: Optional[Dict[str, float]] = None, ratio: Optional[float] = None
    ) -> None:
        """调整权重"""
        if weights is not None:
            self.weights = weights

        if ratio is not None:
            self.ratio = ratio

    def update_weight(self, symbol: str, weight: float) -> None:
        """添加权重"""
        if weight != 0:
            self.weights[symbol] = weight
        else:
            self.weights.pop(symbol, None)


class VXPortfolio:
    """组合信息"""

    def __init__(
        self, subportfolios: Optional[Dict[str, VXSubPortfolio]] = None
    ) -> None:

        self._subportfolios: Dict[str, VXSubPortfolio] = {}
        if subportfolios:
            self._subportfolios.update(subportfolios)

    def __iter__(self) -> Iterator[VXSubPortfolio]:
        return iter(self._subportfolios.values())

    def __getitem__(self, key: str) -> VXSubPortfolio:
        return self._subportfolios[key]

    def __str__(self) -> str:
        return to_json(self.message)

    @classmethod
    def load(cls, config: Union[str, Path]) -> "VXPortfolio":
        """从配置文件中读取组合信息"""
        with open(config, "r") as f:
            data = json.load(f)
        for name, subportfolio in data.items():
            data[name] = VXSubPortfolio(**subportfolio)
        return cls(data)

    def dump(self, path: Union[str, Path]) -> None:
        """将组合信息保存到配置文件"""
        with open(path, "w") as f:
            f.write(to_json(self.message))

    def create_subportfolio(
        self,
        subportfolio_id: str,
        strategy: str,
        ratio: float,
        weights: Optional[Dict[str, float]] = None,
    ) -> VXSubPortfolio:
        """创建子组合"""
        subportfolio = VXSubPortfolio(
            subportfolio_id=subportfolio_id,
            strategy=strategy,
            ratio=ratio,
            weights=weights or {},
        )
        self._subportfolios[subportfolio_id] = subportfolio
        return subportfolio

    def remove_subportfolio(self, subportfolio_id: str) -> None:
        """删除子组合"""
        self._subportfolios.pop(subportfolio_id, None)

    def adjust_ratio(self, subportfolio_id: str, ratio: float) -> None:
        """调整子组合占比"""
        self._subportfolios[subportfolio_id].ratio = ratio

    def rebalance(
        self,
        subportfolio_id: str,
        weights: Optional[Dict[str, float]] = None,
        ratio: Optional[float] = None,
    ) -> None:
        """调整子组合权重"""
        self._subportfolios[subportfolio_id].rebalance(weights, ratio)

    def update_weight(self, subportfolio_id: str, symbol: str, weight: float) -> None:
        """更新子组合权重"""
        self._subportfolios[subportfolio_id].update_weight(symbol, weight)

    @property
    def position_ratio(self) -> float:
        """持仓占比"""
        return sum(sub.ratio for sub in self._subportfolios.values())

    @property
    def weights(self) -> pl.DataFrame:
        """转换为polars格式"""
        data = defaultdict(list)
        for sub in self:
            for symbol, weight in sub.weights.items():
                data["symbol"].append(symbol)
                data["subportfolio_id"].append(sub.subportfolio_id)
                data["strategy"].append(sub.strategy)
                data["ratio"].append(sub.ratio)
                data["weight"].append(weight)
        return (
            pl.DataFrame(data)
            .with_columns(
                [
                    pl.col("weight") / pl.sum("weight").over("subportfolio_id"),
                    (
                        pl.col("ratio")
                        * pl.col("weight")
                        / pl.sum("weight").over("subportfolio_id")
                    ).alias("target_weight"),
                ]
            )
            .group_by("symbol")
            .agg(pl.sum("target_weight").alias("weight"))
            .sort("weight", descending=True)
        )

    @property
    def message(self) -> Dict[str, Any]:
        """组合信息"""
        data = {}
        for name, subportfolio in self._subportfolios.items():
            data[name] = subportfolio.model_dump()

        return data

    def to_df(self) -> pl.DataFrame:
        data = defaultdict(list)
        for sub in self:
            for symbol, weight in sub.weights.items():
                data["symbol"].append(symbol)
                data["subportfolio_id"].append(sub.subportfolio_id)
                data["strategy"].append(sub.strategy)
                data["ratio"].append(sub.ratio)
                data["weight"].append(weight)

        return pl.DataFrame(data).sort(["subportfolio_id", "symbol"])
