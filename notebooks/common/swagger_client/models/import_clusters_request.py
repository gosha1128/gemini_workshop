# coding: utf-8

"""
    GSI Floating-Point 32 API

    **Introduction**<br> GSI Technology’s floating-point similarity search API provides an accessible gateway to running searches on GSI’s Gemini® Associative Processing Unit (APU).<br> It works in conjunction with the GSI system management solution which enables users to work with multiple APU boards simultaneously for improved performance.<br><br> **Dataset and Query Format**<br> Dataset embeddings can be in 32- or 64-bit floating point format, and any number of features, e.g. 256 or 512 (there is no upper limit).<br> Query embeddings must have the same floating-point format and number of features as used in the dataset.<br> GSI performs the search and delivers the top-k most similar results.  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ImportClustersRequest(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'dataset_id': 'str',
        'centroids_float_file_path': 'str',
        'centroids_neural_matrix_file_path': 'str',
        'centroids_neural_matrix_nbits': 'int',
        'centroids_bin_file_path': 'str',
        'clusters_neural_matrix_file_path': 'str',
        'clusters_neural_matrix_nbits': 'int',
        'clusters_bin_file_path': 'str',
        'clusters_records_indexes_file_path': 'str',
        'records_to_clusters_map': 'str',
        'dataset_bin_file_path': 'str'
    }

    attribute_map = {
        'dataset_id': 'datasetId',
        'centroids_float_file_path': 'centroidsFloatFilePath',
        'centroids_neural_matrix_file_path': 'centroidsNeuralMatrixFilePath',
        'centroids_neural_matrix_nbits': 'centroidsNeuralMatrixNbits',
        'centroids_bin_file_path': 'centroidsBinFilePath',
        'clusters_neural_matrix_file_path': 'clustersNeuralMatrixFilePath',
        'clusters_neural_matrix_nbits': 'clustersNeuralMatrixNbits',
        'clusters_bin_file_path': 'clustersBinFilePath',
        'clusters_records_indexes_file_path': 'clustersRecordsIndexesFilePath',
        'records_to_clusters_map': 'recordsToClustersMap',
        'dataset_bin_file_path': 'datasetBinFilePath'
    }

    def __init__(self, dataset_id=None, centroids_float_file_path=None, centroids_neural_matrix_file_path=None, centroids_neural_matrix_nbits=None, centroids_bin_file_path=None, clusters_neural_matrix_file_path=None, clusters_neural_matrix_nbits=None, clusters_bin_file_path=None, clusters_records_indexes_file_path=None, records_to_clusters_map=None, dataset_bin_file_path=None):  # noqa: E501
        """ImportClustersRequest - a model defined in Swagger"""  # noqa: E501
        self._dataset_id = None
        self._centroids_float_file_path = None
        self._centroids_neural_matrix_file_path = None
        self._centroids_neural_matrix_nbits = None
        self._centroids_bin_file_path = None
        self._clusters_neural_matrix_file_path = None
        self._clusters_neural_matrix_nbits = None
        self._clusters_bin_file_path = None
        self._clusters_records_indexes_file_path = None
        self._records_to_clusters_map = None
        self._dataset_bin_file_path = None
        self.discriminator = None
        self.dataset_id = dataset_id
        self.centroids_float_file_path = centroids_float_file_path
        self.centroids_neural_matrix_file_path = centroids_neural_matrix_file_path
        if centroids_neural_matrix_nbits is not None:
            self.centroids_neural_matrix_nbits = centroids_neural_matrix_nbits
        self.centroids_bin_file_path = centroids_bin_file_path
        self.clusters_neural_matrix_file_path = clusters_neural_matrix_file_path
        if clusters_neural_matrix_nbits is not None:
            self.clusters_neural_matrix_nbits = clusters_neural_matrix_nbits
        if clusters_bin_file_path is not None:
            self.clusters_bin_file_path = clusters_bin_file_path
        if clusters_records_indexes_file_path is not None:
            self.clusters_records_indexes_file_path = clusters_records_indexes_file_path
        if records_to_clusters_map is not None:
            self.records_to_clusters_map = records_to_clusters_map
        if dataset_bin_file_path is not None:
            self.dataset_bin_file_path = dataset_bin_file_path

    @property
    def dataset_id(self):
        """Gets the dataset_id of this ImportClustersRequest.  # noqa: E501

        The datasetId identifies the specific dataset to search. It is generated using the /import/dataset endpoint.  # noqa: E501

        :return: The dataset_id of this ImportClustersRequest.  # noqa: E501
        :rtype: str
        """
        return self._dataset_id

    @dataset_id.setter
    def dataset_id(self, dataset_id):
        """Sets the dataset_id of this ImportClustersRequest.

        The datasetId identifies the specific dataset to search. It is generated using the /import/dataset endpoint.  # noqa: E501

        :param dataset_id: The dataset_id of this ImportClustersRequest.  # noqa: E501
        :type: str
        """
        if dataset_id is None:
            raise ValueError("Invalid value for `dataset_id`, must not be `None`")  # noqa: E501

        self._dataset_id = dataset_id

    @property
    def centroids_float_file_path(self):
        """Gets the centroids_float_file_path of this ImportClustersRequest.  # noqa: E501

        Path to a file containing the centroids records in type float.  # noqa: E501

        :return: The centroids_float_file_path of this ImportClustersRequest.  # noqa: E501
        :rtype: str
        """
        return self._centroids_float_file_path

    @centroids_float_file_path.setter
    def centroids_float_file_path(self, centroids_float_file_path):
        """Sets the centroids_float_file_path of this ImportClustersRequest.

        Path to a file containing the centroids records in type float.  # noqa: E501

        :param centroids_float_file_path: The centroids_float_file_path of this ImportClustersRequest.  # noqa: E501
        :type: str
        """
        if centroids_float_file_path is None:
            raise ValueError("Invalid value for `centroids_float_file_path`, must not be `None`")  # noqa: E501

        self._centroids_float_file_path = centroids_float_file_path

    @property
    def centroids_neural_matrix_file_path(self):
        """Gets the centroids_neural_matrix_file_path of this ImportClustersRequest.  # noqa: E501

        Path to a neural matrix file trained for the centroids.  # noqa: E501

        :return: The centroids_neural_matrix_file_path of this ImportClustersRequest.  # noqa: E501
        :rtype: str
        """
        return self._centroids_neural_matrix_file_path

    @centroids_neural_matrix_file_path.setter
    def centroids_neural_matrix_file_path(self, centroids_neural_matrix_file_path):
        """Sets the centroids_neural_matrix_file_path of this ImportClustersRequest.

        Path to a neural matrix file trained for the centroids.  # noqa: E501

        :param centroids_neural_matrix_file_path: The centroids_neural_matrix_file_path of this ImportClustersRequest.  # noqa: E501
        :type: str
        """
        if centroids_neural_matrix_file_path is None:
            raise ValueError("Invalid value for `centroids_neural_matrix_file_path`, must not be `None`")  # noqa: E501

        self._centroids_neural_matrix_file_path = centroids_neural_matrix_file_path

    @property
    def centroids_neural_matrix_nbits(self):
        """Gets the centroids_neural_matrix_nbits of this ImportClustersRequest.  # noqa: E501

        Centroids neural matrix number of bits.  # noqa: E501

        :return: The centroids_neural_matrix_nbits of this ImportClustersRequest.  # noqa: E501
        :rtype: int
        """
        return self._centroids_neural_matrix_nbits

    @centroids_neural_matrix_nbits.setter
    def centroids_neural_matrix_nbits(self, centroids_neural_matrix_nbits):
        """Sets the centroids_neural_matrix_nbits of this ImportClustersRequest.

        Centroids neural matrix number of bits.  # noqa: E501

        :param centroids_neural_matrix_nbits: The centroids_neural_matrix_nbits of this ImportClustersRequest.  # noqa: E501
        :type: int
        """

        self._centroids_neural_matrix_nbits = centroids_neural_matrix_nbits

    @property
    def centroids_bin_file_path(self):
        """Gets the centroids_bin_file_path of this ImportClustersRequest.  # noqa: E501

        Path to centroids bin file path.  # noqa: E501

        :return: The centroids_bin_file_path of this ImportClustersRequest.  # noqa: E501
        :rtype: str
        """
        return self._centroids_bin_file_path

    @centroids_bin_file_path.setter
    def centroids_bin_file_path(self, centroids_bin_file_path):
        """Sets the centroids_bin_file_path of this ImportClustersRequest.

        Path to centroids bin file path.  # noqa: E501

        :param centroids_bin_file_path: The centroids_bin_file_path of this ImportClustersRequest.  # noqa: E501
        :type: str
        """
        if centroids_bin_file_path is None:
            raise ValueError("Invalid value for `centroids_bin_file_path`, must not be `None`")  # noqa: E501

        self._centroids_bin_file_path = centroids_bin_file_path

    @property
    def clusters_neural_matrix_file_path(self):
        """Gets the clusters_neural_matrix_file_path of this ImportClustersRequest.  # noqa: E501

        Path to a neural matrix file trained for the clusters.  # noqa: E501

        :return: The clusters_neural_matrix_file_path of this ImportClustersRequest.  # noqa: E501
        :rtype: str
        """
        return self._clusters_neural_matrix_file_path

    @clusters_neural_matrix_file_path.setter
    def clusters_neural_matrix_file_path(self, clusters_neural_matrix_file_path):
        """Sets the clusters_neural_matrix_file_path of this ImportClustersRequest.

        Path to a neural matrix file trained for the clusters.  # noqa: E501

        :param clusters_neural_matrix_file_path: The clusters_neural_matrix_file_path of this ImportClustersRequest.  # noqa: E501
        :type: str
        """
        if clusters_neural_matrix_file_path is None:
            raise ValueError("Invalid value for `clusters_neural_matrix_file_path`, must not be `None`")  # noqa: E501

        self._clusters_neural_matrix_file_path = clusters_neural_matrix_file_path

    @property
    def clusters_neural_matrix_nbits(self):
        """Gets the clusters_neural_matrix_nbits of this ImportClustersRequest.  # noqa: E501

        Clusters neural matrix number of bits.  # noqa: E501

        :return: The clusters_neural_matrix_nbits of this ImportClustersRequest.  # noqa: E501
        :rtype: int
        """
        return self._clusters_neural_matrix_nbits

    @clusters_neural_matrix_nbits.setter
    def clusters_neural_matrix_nbits(self, clusters_neural_matrix_nbits):
        """Sets the clusters_neural_matrix_nbits of this ImportClustersRequest.

        Clusters neural matrix number of bits.  # noqa: E501

        :param clusters_neural_matrix_nbits: The clusters_neural_matrix_nbits of this ImportClustersRequest.  # noqa: E501
        :type: int
        """

        self._clusters_neural_matrix_nbits = clusters_neural_matrix_nbits

    @property
    def clusters_bin_file_path(self):
        """Gets the clusters_bin_file_path of this ImportClustersRequest.  # noqa: E501

        Path to clusters bin file path.  # noqa: E501

        :return: The clusters_bin_file_path of this ImportClustersRequest.  # noqa: E501
        :rtype: str
        """
        return self._clusters_bin_file_path

    @clusters_bin_file_path.setter
    def clusters_bin_file_path(self, clusters_bin_file_path):
        """Sets the clusters_bin_file_path of this ImportClustersRequest.

        Path to clusters bin file path.  # noqa: E501

        :param clusters_bin_file_path: The clusters_bin_file_path of this ImportClustersRequest.  # noqa: E501
        :type: str
        """

        self._clusters_bin_file_path = clusters_bin_file_path

    @property
    def clusters_records_indexes_file_path(self):
        """Gets the clusters_records_indexes_file_path of this ImportClustersRequest.  # noqa: E501

        Path to file containing list of clusters holding the original index of each cluster record.  # noqa: E501

        :return: The clusters_records_indexes_file_path of this ImportClustersRequest.  # noqa: E501
        :rtype: str
        """
        return self._clusters_records_indexes_file_path

    @clusters_records_indexes_file_path.setter
    def clusters_records_indexes_file_path(self, clusters_records_indexes_file_path):
        """Sets the clusters_records_indexes_file_path of this ImportClustersRequest.

        Path to file containing list of clusters holding the original index of each cluster record.  # noqa: E501

        :param clusters_records_indexes_file_path: The clusters_records_indexes_file_path of this ImportClustersRequest.  # noqa: E501
        :type: str
        """

        self._clusters_records_indexes_file_path = clusters_records_indexes_file_path

    @property
    def records_to_clusters_map(self):
        """Gets the records_to_clusters_map of this ImportClustersRequest.  # noqa: E501

        Path to file containing a map between the dataset records to the clusters.  # noqa: E501

        :return: The records_to_clusters_map of this ImportClustersRequest.  # noqa: E501
        :rtype: str
        """
        return self._records_to_clusters_map

    @records_to_clusters_map.setter
    def records_to_clusters_map(self, records_to_clusters_map):
        """Sets the records_to_clusters_map of this ImportClustersRequest.

        Path to file containing a map between the dataset records to the clusters.  # noqa: E501

        :param records_to_clusters_map: The records_to_clusters_map of this ImportClustersRequest.  # noqa: E501
        :type: str
        """

        self._records_to_clusters_map = records_to_clusters_map

    @property
    def dataset_bin_file_path(self):
        """Gets the dataset_bin_file_path of this ImportClustersRequest.  # noqa: E501

        Path to the dataset bin file  # noqa: E501

        :return: The dataset_bin_file_path of this ImportClustersRequest.  # noqa: E501
        :rtype: str
        """
        return self._dataset_bin_file_path

    @dataset_bin_file_path.setter
    def dataset_bin_file_path(self, dataset_bin_file_path):
        """Sets the dataset_bin_file_path of this ImportClustersRequest.

        Path to the dataset bin file  # noqa: E501

        :param dataset_bin_file_path: The dataset_bin_file_path of this ImportClustersRequest.  # noqa: E501
        :type: str
        """

        self._dataset_bin_file_path = dataset_bin_file_path

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(ImportClustersRequest, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ImportClustersRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other