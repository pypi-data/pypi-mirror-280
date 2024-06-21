# Copyright The PyTorch Lightning team.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from torchmetrics_sdv2.functional.audio.pesq import pesq
from torchmetrics_sdv2.functional.audio.pit import pit, pit_permutate
from torchmetrics_sdv2.functional.audio.si_sdr import si_sdr
from torchmetrics_sdv2.functional.audio.si_snr import si_snr
from torchmetrics_sdv2.functional.audio.snr import snr
from torchmetrics_sdv2.functional.audio.stoi import stoi
from torchmetrics_sdv2.functional.classification.accuracy import accuracy
from torchmetrics_sdv2.functional.classification.auc import auc
from torchmetrics_sdv2.functional.classification.auroc import auroc
from torchmetrics_sdv2.functional.classification.average_precision import average_precision
from torchmetrics_sdv2.functional.classification.calibration_error import calibration_error
from torchmetrics_sdv2.functional.classification.cohen_kappa import cohen_kappa
from torchmetrics_sdv2.functional.classification.confusion_matrix import confusion_matrix
from torchmetrics_sdv2.functional.classification.dice import dice_score
from torchmetrics_sdv2.functional.classification.f_beta import f1, fbeta
from torchmetrics_sdv2.functional.classification.hamming_distance import hamming_distance
from torchmetrics_sdv2.functional.classification.hinge import hinge
from torchmetrics_sdv2.functional.classification.iou import iou
from torchmetrics_sdv2.functional.classification.kl_divergence import kl_divergence
from torchmetrics_sdv2.functional.classification.matthews_corrcoef import matthews_corrcoef
from torchmetrics_sdv2.functional.classification.precision_recall import precision, precision_recall, recall
from torchmetrics_sdv2.functional.classification.precision_recall_curve import precision_recall_curve
from torchmetrics_sdv2.functional.classification.roc import roc
from torchmetrics_sdv2.functional.classification.specificity import specificity
from torchmetrics_sdv2.functional.classification.stat_scores import stat_scores
from torchmetrics_sdv2.functional.image.gradients import image_gradients
from torchmetrics_sdv2.functional.image.psnr import psnr
from torchmetrics_sdv2.functional.image.ssim import ssim
from torchmetrics_sdv2.functional.pairwise.cosine import pairwise_cosine_similarity
from torchmetrics_sdv2.functional.pairwise.euclidean import pairwise_euclidean_distance
from torchmetrics_sdv2.functional.pairwise.linear import pairwise_linear_similarity
from torchmetrics_sdv2.functional.pairwise.manhatten import pairwise_manhatten_distance
from torchmetrics_sdv2.functional.regression.cosine_similarity import cosine_similarity
from torchmetrics_sdv2.functional.regression.explained_variance import explained_variance
from torchmetrics_sdv2.functional.regression.mean_absolute_error import mean_absolute_error
from torchmetrics_sdv2.functional.regression.mean_absolute_percentage_error import mean_absolute_percentage_error
from torchmetrics_sdv2.functional.regression.mean_squared_error import mean_squared_error
from torchmetrics_sdv2.functional.regression.mean_squared_log_error import mean_squared_log_error
from torchmetrics_sdv2.functional.regression.pearson import pearson_corrcoef
from torchmetrics_sdv2.functional.regression.r2 import r2_score
from torchmetrics_sdv2.functional.regression.spearman import spearman_corrcoef
from torchmetrics_sdv2.functional.regression.symmetric_mean_absolute_percentage_error import (
    symmetric_mean_absolute_percentage_error,
)
from torchmetrics_sdv2.functional.regression.tweedie_deviance import tweedie_deviance_score
from torchmetrics_sdv2.functional.retrieval.average_precision import retrieval_average_precision
from torchmetrics_sdv2.functional.retrieval.fall_out import retrieval_fall_out
from torchmetrics_sdv2.functional.retrieval.hit_rate import retrieval_hit_rate
from torchmetrics_sdv2.functional.retrieval.ndcg import retrieval_normalized_dcg
from torchmetrics_sdv2.functional.retrieval.precision import retrieval_precision
from torchmetrics_sdv2.functional.retrieval.r_precision import retrieval_r_precision
from torchmetrics_sdv2.functional.retrieval.recall import retrieval_recall
from torchmetrics_sdv2.functional.retrieval.reciprocal_rank import retrieval_reciprocal_rank
from torchmetrics_sdv2.functional.self_supervised import embedding_similarity
from torchmetrics_sdv2.functional.text.bert import bert_score
from torchmetrics_sdv2.functional.text.bleu import bleu_score
from torchmetrics_sdv2.functional.text.cer import char_error_rate
from torchmetrics_sdv2.functional.text.rouge import rouge_score
from torchmetrics_sdv2.functional.text.sacre_bleu import sacre_bleu_score
from torchmetrics_sdv2.functional.text.wer import wer

__all__ = [
    "accuracy",
    "auc",
    "auroc",
    "average_precision",
    "bert_score",
    "bleu_score",
    "calibration_error",
    "cohen_kappa",
    "confusion_matrix",
    "cosine_similarity",
    "tweedie_deviance_score",
    "dice_score",
    "embedding_similarity",
    "explained_variance",
    "f1",
    "fbeta",
    "hamming_distance",
    "hinge",
    "image_gradients",
    "iou",
    "kl_divergence",
    "kldivergence",
    "matthews_corrcoef",
    "mean_absolute_error",
    "mean_absolute_percentage_error",
    "mean_squared_error",
    "mean_squared_log_error",
    "pairwise_cosine_similarity",
    "pairwise_euclidean_distance",
    "pairwise_linear_similarity",
    "pairwise_manhatten_distance",
    "pearson_corrcoef",
    "pesq",
    "pit",
    "pit_permutate",
    "precision",
    "precision_recall",
    "precision_recall_curve",
    "psnr",
    "r2_score",
    "r2score",
    "recall",
    "retrieval_average_precision",
    "retrieval_fall_out",
    "retrieval_hit_rate",
    "retrieval_normalized_dcg",
    "retrieval_precision",
    "retrieval_r_precision",
    "retrieval_recall",
    "retrieval_reciprocal_rank",
    "roc",
    "rouge_score",
    "sacre_bleu_score",
    "si_sdr",
    "si_snr",
    "snr",
    "spearman_corrcoef",
    "specificity",
    "ssim",
    "stat_scores",
    "stoi",
    "symmetric_mean_absolute_percentage_error",
    "wer",
    "char_error_rate",
]
