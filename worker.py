
def check_clusters():
    """
    This function checks available clusters and return the list of cluster names

    **Returns:**

    * 'cluster_list' : list o cluster names
    """
    pass

def get_cluster_machines(cluster_name):
    """
    This function checks the cluster name and return the list of associated machines to the cluster

    **Args:**

    * 'cluster_name' : list of strings represent the cluster name

    **Returns:**

    * 'machine_addresses' : the dictionary with the machines associated with cluster.
    The keywords are cluster names, the values are lists containing strings with machines names.
    """
    pass

def add_cluster(cluster_name, cluster_list):
    """
    This function checks if the cluster name already exists and if now adds new cluster name.

    :param cluster_name: the string representing the name of new cluster.
    :param cluster_list: the list of existing clusters.
    :return: the cluster list.
    """
    pass

def remove_cluster(cluster_name, cluster_list):
    """
    This function checks if the cluster name exists and then remove it.

    :param cluster_name: the string representing the name of cluster that should be removed.
    :param cluster_list: the list of cluster
    :return: updated cluster_list
    """
    pass


def add_machine(cluster_name, machine_address):
    """
    This function add the machine_address (string) to the cluster specified in cluster_name (string).
    At first it check if the machine_address already exists in the cluster.

    :param cluster_name: the name of cluster where the new machine belongs to.
    :param machine_address: the address of the machine that belongs to cluster specified by cluster_name
    :return: True/False based on the result of addition
    """
    pass


def remove_machine(cluster_name, machine_address):
    """
    This function removes the machine from the specified cluster.
    :param cluster_name: the cluster name which the machine belongs to.
    :param machine_address: the address of machine to be revomed from the cluster.
    :return: True/False based on the success of the removal
    """
    pass


def perform_ping(cluster_name, machine_address):
    """
    This function perform the ping to the machine that is specified by the cluster name and machine address.

    :param cluster_name: the name of the cluster
    :param machine_address: the address of the machine that belong to the specified cluster
    :return: the result of the ping
    """
    pass


def perform_cluster_ping(cluster_name):
    """
    This function performs the ping to all machines that belongs to cluster.

    :param cluster_name: name of the cluster (string)
    :return: return the list of ping results
    """
    pass


