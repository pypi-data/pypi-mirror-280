r"""Root package info."""
import logging as __logging
import os

from torchmetrics_sdv2.__about__ import *  # noqa: F401, F403

_logger = __logging.getLogger("torchmetrics")
_logger.addHandler(__logging.StreamHandler())
_logger.setLevel(__logging.INFO)

_PACKAGE_ROOT = os.path.dirname(__file__)
_PROJECT_ROOT = os.path.dirname(_PACKAGE_ROOT)

from torchmetrics_sdv2 import functional  # noqa: E402
from torchmetrics_sdv2.aggregation import CatMetric, MaxMetric, MeanMetric, MinMetric, SumMetric  # noqa: E402
from torchmetrics_sdv2.audio import PESQ, PIT, SI_SDR, SI_SNR, SNR, STOI  # noqa: E402
from torchmetrics_sdv2.classification import (  # noqa: E402
    AUC,
    AUROC,
    F1,
    ROC,
    Accuracy,
    AveragePrecision,
    BinnedAveragePrecision,
    BinnedPrecisionRecallCurve,
    BinnedRecallAtFixedPrecision,
    CalibrationError,
    CohenKappa,
    ConfusionMatrix,
    FBeta,
    HammingDistance,
    Hinge,
    IoU,
    KLDivergence,
    MatthewsCorrcoef,
    Precision,
    PrecisionRecallCurve,
    Recall,
    Specificity,
    StatScores,
)
from torchmetrics_sdv2.collections import MetricCollection  # noqa: E402
from torchmetrics_sdv2.detection import MAP  # noqa: E402
from torchmetrics_sdv2.image import FID, IS, KID, LPIPS, PSNR, SSIM  # noqa: E402
from torchmetrics_sdv2.metric import Metric  # noqa: E402
from torchmetrics_sdv2.regression import (  # noqa: E402
    CosineSimilarity,
    ExplainedVariance,
    MeanAbsoluteError,
    MeanAbsolutePercentageError,
    MeanSquaredError,
    MeanSquaredLogError,
    PearsonCorrcoef,
    R2Score,
    SpearmanCorrcoef,
    SymmetricMeanAbsolutePercentageError,
    TweedieDevianceScore,
)
from torchmetrics_sdv2.retrieval import (  # noqa: E402
    RetrievalFallOut,
    RetrievalHitRate,
    RetrievalMAP,
    RetrievalMRR,
    RetrievalNormalizedDCG,
    RetrievalPrecision,
    RetrievalRecall,
    RetrievalRPrecision,
)
from torchmetrics_sdv2.text import WER, BERTScore, BLEUScore, CharErrorRate, ROUGEScore, SacreBLEUScore  # noqa: E402
from torchmetrics_sdv2.wrappers import BootStrapper, MetricTracker, MultioutputWrapper  # noqa: E402

__all__ = [
    "functional",
    "Accuracy",
    "AUC",
    "AUROC",
    "AveragePrecision",
    "BinnedAveragePrecision",
    "BinnedPrecisionRecallCurve",
    "BinnedRecallAtFixedPrecision",
    "BERTScore",
    "BLEUScore",
    "BootStrapper",
    "CalibrationError",
    "CatMetric",
    "CohenKappa",
    "ConfusionMatrix",
    "CosineSimilarity",
    "TweedieDevianceScore",
    "ExplainedVariance",
    "F1",
    "FBeta",
    "FID",
    "HammingDistance",
    "Hinge",
    "IoU",
    "IS",
    "KID",
    "KLDivergence",
    "LPIPS",
    "MAP",
    "MatthewsCorrcoef",
    "MaxMetric",
    "MeanAbsoluteError",
    "MeanAbsolutePercentageError",
    "MeanMetric",
    "MeanSquaredError",
    "MeanSquaredLogError",
    "Metric",
    "MetricCollection",
    "MetricTracker",
    "MinMetric",
    "MultioutputWrapper",
    "PearsonCorrcoef",
    "PESQ",
    "PIT",
    "Precision",
    "PrecisionRecallCurve",
    "PSNR",
    "R2Score",
    "Recall",
    "RetrievalFallOut",
    "RetrievalHitRate",
    "RetrievalMAP",
    "RetrievalMRR",
    "RetrievalNormalizedDCG",
    "RetrievalPrecision",
    "RetrievalRecall",
    "RetrievalRPrecision",
    "ROC",
    "ROUGEScore",
    "SacreBLEUScore",
    "SI_SDR",
    "SI_SNR",
    "SNR",
    "SpearmanCorrcoef",
    "Specificity",
    "SSIM",
    "StatScores",
    "STOI",
    "SumMetric",
    "SymmetricMeanAbsolutePercentageError",
    "WER",
    "CharErrorRate",
]
