import pandas as pd

from Time2Feat.utils.importance_old import feature_selection
from Time2Feat.extraction.extractor import feature_extraction
from Time2Feat.model.clustering import ClusterWrapper
class Time2Feat(object):

    def __init__(self, n_clusters, batch_size=100, p=1, model_type='KMeans', transform_type='std', score_mode='simple', strategy='sk_base',
                 k_best=False, pre_transform=False, top_k=None, pfa_value=0.9):
        """
        Initialize Time2Feat method with specified parameters.

        Parameters:
        - n_clusters (int): Number of clusters to be used.
        - batch_size (int, optional): Batch size for processing (default is 100).
        - p (int, optional): Some parameter `p` (default is 1).
        - model_type (str, optional): Type of model to use (default is 'kMeans').
        - transform_type (str, optional): Type of data normalization (default is 'std').
        - score_mode (str, optional): Mode for scoring (default is 'simple').
        - strategy (str, optional): Strategy of features selection to be used (default is 'sk_base').
        - k_best (bool, optional): Whether to use k-best selection (default is False).
        - pre_transform (bool, optional): Whether to apply pre-transformation (default is False).
        - top_k (list of int, optional): List of top-k values (default is [1]).
        - pfa_value (float, optional): Some value `pfa_value` (default is 0.9).
        """
        if top_k is None:
            top_k = [1]
        self.n_clusters = n_clusters
        self.batch_size = batch_size
        self.p = p
        self.model_type = model_type
        self.transform_type = transform_type
        self.score_mode = score_mode
        self.strategy = strategy
        self.k_best = k_best
        self.pre_transform = pre_transform
        self.top_k = top_k
        self.pfa_value = pfa_value
        self.top_feats = []


    def fit(self,X, labels={}, external_feat: pd.DataFrame = None):
        df_feats = feature_extraction(X, batch_size=self.batch_size, p=self.p)
        context = {'model_type': self.model_type, 'transform_type': self.transform_type, 'score_mode': self.score_mode,
                   'strategy': self.strategy, 'k_best': self.k_best, 'pre_transform': self.pre_transform,
                   'top_k': self.top_k, 'pfa_value': self.pfa_value}
        top_feats = feature_selection(df_feats, labels=labels, context=context, external_feat=external_feat)
        df_feats = df_feats[top_feats]
        if external_feat is not None:
            df_feats = pd.concat([df_feats, external_feat], axis=1)

        return df_feats

    def fit_predict(self,X, labels={}, external_feat: pd.DataFrame = None):
        df_feats = self.fit(X, labels, external_feat)
        model = ClusterWrapper(n_clusters=self.n_clusters, model_type=self.model_type,
                               transform_type=self.transform_type)
        y_pred = model.fit_predict(df_feats)
        return y_pred
