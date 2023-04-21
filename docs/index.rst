.. Kubeflow documentation master file, created by
   sphinx-quickstart on Fri Jan 13 06:56:36 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. image:: /_static/kubeflow-logo.png
   :align: center
   :scale: 20%

Welcome
=======

Data scientists often face the challenge to manually execute all the steps in a machine learning workflow, including moving and transforming data, training models, and promoting them to production. This is where Kubeflow comes in. Kubeflow is a free and open-source machine learning platform that streamlines the entire machine learning process, from data preparation and modeling to deployment. It uses pipelines to orchestrate complicated machine learning workflows and is dedicated to simplifying the deployments by providing a straightforward approach.

Kubeflow is a powerful machine learning operations (MLOps) platform that can be used for experimentation, development, and production. Based on Kubeflow, we’ve developed vSphere Enterprise Kubeflow version, which is a VMware-sponsored initiative aimed at meeting the strict business and technical requirements for enterprise infrastructure. To address the challenges faced by enterprises, we've made several enhancements, including:

- Optimized GPU utilization with GPU sharing management, enabling enterprises to optimize the machine learning workflows for better performance.
- A rich offering of poplular training models, covering a wide range of use cases.
- Streamlined packaging and deployment user experience, making the deployment of Kubeflow on vSphere easier and swifter.

Additionally, vSphere Enterprise Kubeflow incorporates several Kubeflow add-ons and community softwares to create an Enterprise-ready MLOps platform on vSphere. With vSphere Enterprise Kubeflow, enterprises can enjoy the benefits of an efficient and streamlined machine learning workflow, allowing them to achieve faster and more accurate results.

This documentation presents a comprehensive end-to-end workflow of using vSphere Enterprise Kubeflow to build, train, and deploy machine learning models. It will guide you through the entire process, from data preparation to model serving, and explain how various components of vSphere Enterprise Kubeflow work together to streamline and enhance your machine learning workflow. Furthermore, we will provide our best practices for deploying Kubeflow components locally, on-prem, and in the cloud. By the end of this documentation, you will have a better understanding of how to use vSphere Enterprise Kubeflow to manage your machine learning projects and you'll be able to apply the additional provided features to your projects.


.. toctree::
    :caption: Kubeflow Docs
    :hidden:

    introduction/index
    introduction/oss
    introduction/ekf
    introduction/mlops

.. toctree::
    :caption: Install and Configure
    :hidden:

    install/index
    install/tkgs
    install/auth
    install/monitor

.. toctree::
    :caption: User Guide
    :hidden:

    user-guide/index
    user-guide/notebooks
    user-guide/feast
    user-guide/spark
    user-guide/mlmd
    user-guide/mlflow
    user-guide/training
    user-guide/tensorboard
    user-guide/katib
    user-guide/kserve
    user-guide/kfp

.. toctree::
    :caption: Use Cases
    :hidden:

    use-cases/index
    use-cases/helmet
    use-cases/modelserving
    use-cases/codegen

.. toctree::
    :caption: Internals
    :hidden:

    internals/auth

License
-------

Open Source (OSS) Kubeflow is released under the Apache License 2.0.

Kubeflow Enterprise and its documents are offered as free, open-source software. You don’t need a support agreement or license to deploy them.

.. Indices and tables
   ==================

   * :ref:`genindex`
   * :ref:`modindex`
   * :ref:`search`
