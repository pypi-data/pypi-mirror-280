import abc
import dataclasses

import numpy as np
import numpy.typing as npt
from finitedepth import CoatingLayerBase, RectSubstrate
from finitedepth.coatinglayer import DataTypeVar, SubstTypeVar

class IfdRoughnessBase(
    CoatingLayerBase[SubstTypeVar, DataTypeVar], metaclass=abc.ABCMeta
):
    DataType: type[DataTypeVar]
    delta: float
    def __init__(
        self,
        image: npt.NDArray[np.uint8],
        substrate: SubstTypeVar,
        delta: float,
        *,
        tempmatch: tuple[tuple[int, int], float] | None = None,
    ) -> None: ...
    @abc.abstractmethod
    def surface(self) -> npt.NDArray[np.int32]: ...
    @abc.abstractmethod
    def uniform_layer(self) -> npt.NDArray[np.float64]: ...
    def roughness(self) -> tuple[float, npt.NDArray[np.float64]]: ...

@dataclasses.dataclass
class RectIfdRoughnessData:
    AverageThickness: float
    Roughness: float
    def __init__(self, AverageThickness, Roughness) -> None: ...

class RectIfdRoughness(IfdRoughnessBase[RectSubstrate, RectIfdRoughnessData]):
    DataType = RectIfdRoughnessData
    opening_ksize: tuple[int, int]
    reconstruct_radius: int
    def __init__(
        self,
        image: npt.NDArray[np.uint8],
        substrate: RectSubstrate,
        delta: float,
        opening_ksize: tuple[int, int],
        reconstruct_radius: int,
        *,
        tempmatch: tuple[tuple[int, int], float] | None = None,
    ) -> None: ...
    def valid(self) -> bool: ...
    def extract_layer(self) -> npt.NDArray[np.bool_]: ...
    def substrate_contour(self) -> npt.NDArray[np.int_]: ...
    def interface_indices(self) -> npt.NDArray[np.int_]: ...
    def surface(self) -> npt.NDArray[np.int32]: ...
    def average_thickness(self) -> float: ...
    def uniform_layer(self) -> npt.NDArray[np.float64]: ...
    def analyze(self) -> RectIfdRoughnessData: ...
    def draw(self, pairs_dist: float = 20.0) -> npt.NDArray[np.uint8]: ...
