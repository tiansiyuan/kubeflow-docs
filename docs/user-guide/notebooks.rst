.. _user-guide-notebooks:

==================
Kubeflow Notebooks
==================

Introduction
------------
Kubeflow Notebooks provide a way to run web-based development environments, Jupyter Notebook inside your Kubernetes cluster by running them inside Pods.

Jupyter Notebook is an interactive web-based computational environment that allows users to create and share documents that contain live code, equations, visualizations, and narrative text. It supports many programming languages, including Python, R, and Julia, among others.

Jupyter Notebook is particularly popular among data scientists, researchers, and educators because of its ability to combine code with rich text, making it easy to communicate ideas, results, and analyses with others. It also allows users to run code in small, testable chunks, making it easy to experiment and debug code.

Get Started
-----------

Create a Kubeflow Notebook
^^^^^^^^^^^^^^^^^^^^^^^^^^

The dashboard will give you an overview of the Notebook Servers currently available on your Kubeflow installation. In a freshly installed Kubeflow there will be no Notebook Server.
You will create a new Notebook Server by clicking on "Notebooks" in the left-side navigation and then clicking on the "New Notebook" button.

In the "New Notebook" section you will be able to specify several options for the notebook you are creating. In the image section choose an image of ``jupyter-tensorflow-full``. It is required for our example notebook. (More details about container images used for Notebook Server are introduced in following sections.) Please leave the CPU and memory requirements to the default ones.

Once the Notebook Server is created, you connect to it by clicking on the "Connect" button from the left side to it and access your Jupyter Notebook environment which will be opened in a new tab.

.. image:: ../_static/notebook-1.png

For testing the server we will upload the `Tensorflow 2 quickstart for experts example <https://www.tensorflow.org/tutorials/quickstart/advanced>`_.

Click on the link above and click on the "Download Notebook" button just below the heading. This will download the file ``advanced.ipynb`` into your usual Download location. This file will be used to create the example notebook.

On the "Notebook Server" page, click on the "Upload" button, which is located in the side-bar at the top, and select the ``advanced.ipnyb`` file.

.. image:: ../_static/notebook-2.png

Once uploaded, click on the notebook name to open a new tab with the notebook content.

.. image:: ../_static/notebook-3.png

You can read through the content for a better understanding of what this notebook does. Click on the Run button "▶︎"  to execute each stage of the document, or click on the double-chevron ">>" to execute the entire document.

Kubeflow Notebook Volume
^^^^^^^^^^^^^^^^^^^^^^^^

In order to see the volume of the notebook that you just created in the previous step, please click on "Volumes" on the left side-bar. You will see a volume that has the same name as the notebook with ``-volume`` at the end.

.. image:: ../_static/notebook-4.png

Delete Kubeflow Notebook
^^^^^^^^^^^^^^^^^^^^^^^^

In order to delete a new notebook, you will click on "Notebooks" in the left-side navigation. Go to the notebook you want to delete, an click on the small trash bin icon situated alongside the notebook.

.. image:: ../_static/notebook-5.png

A new window will appear on your screen. Click "Delete".

.. image:: ../_static/notebook-6.png

Container Images
^^^^^^^^^^^^^^^^

In above sections, we choose an image of ``jupyter-tensorflow-full`` when creating the Notebook Server. In this section, we will introduce you to 
container images more in details.

Kubeflow Notebooks natively supports three types of notebooks: `JupyterLab <https://github.com/jupyterlab/jupyterlab>`_, 
`RStudio <https://github.com/rstudio/rstudio>`_, and `Visual Studio Code (code-server) <https://github.com/coder/code-server>`_. But any web-based IDE 
should work. Notebook Servers run as containers inside a Kubernetes Pod, which means the type of IDE (and which packages are installed) is determined by 
the Docker image you pick for your server.

Provided Images
~~~~~~~~~~~~~~~

Kubeflow provides a number of `example container images <https://github.com/kubeflow/kubeflow/tree/master/components/example-notebook-servers>`_ as shown in the below table for you 
to get started. In addition, the link in the table guides you to a Git repo in which you can find the Dockerfile of each provided example container image.

.. list-table::
   :widths: auto
   :header-rows: 1

   * - Dockerfile
     - Registry
     - Notes
   * - `jupyter-scipy <https://github.com/kubeflow/kubeflow/tree/master/components/example-notebook-servers/jupyter-scipy>`_
     - kubeflownotebookswg/jupyter-scipy:{TAG}
     - JupyterLab + `SciPy <https://scipy.org/>`_ packages
   * - `jupyter-pytorch-full (CPU) <https://github.com/kubeflow/kubeflow/tree/master/components/example-notebook-servers/jupyter-pytorch-full>`_
     - kubeflownotebookswg/jupyter-pytorch-full:{TAG}
     - JupyterLab + PyTorch (CPU)  `common <https://github.com/kubeflow/kubeflow/blob/master/components/example-notebook-servers/jupyter-pytorch-full/requirements.txt>`__ packages
   * - `jupyter-pytorch-full (CUDA) <https://github.com/kubeflow/kubeflow/tree/master/components/example-notebook-servers/jupyter-pytorch-full>`_
     - kubeflownotebookswg/jupyter-pytorch-cuda-full:{TAG}
     - JupyterLab + PyTorch (CUDA) + `common <https://github.com/kubeflow/kubeflow/blob/master/components/example-notebook-servers/jupyter-pytorch-full/requirements.txt>`__ packages
   * - `jupyter-tensorflow-full (CPU) <https://github.com/kubeflow/kubeflow/tree/master/components/example-notebook-servers/jupyter-tensorflow-full>`_
     - kubeflownotebookswg/jupyter-tensorflow-full:{TAG}
     - JupyterLab + TensorFlow (CPU) + `common <https://github.com/kubeflow/kubeflow/blob/master/components/example-notebook-servers/jupyter-tensorflow-full/requirements.txt>`_ packages
   * - `jupyter-tensorflow-full (CUDA) <https://github.com/kubeflow/kubeflow/tree/master/components/example-notebook-servers/jupyter-tensorflow-full>`_
     - kubeflownotebookswg/jupyter-tensorflow-cuda-full:{TAG}
     - JupyterLab + TensorFlow (CUDA) + `common <https://github.com/kubeflow/kubeflow/blob/master/components/example-notebook-servers/jupyter-tensorflow-full/requirements.txt>`_ packages
   * - `codeserver-python <https://github.com/kubeflow/kubeflow/tree/master/components/example-notebook-servers/codeserver-python>`_
     - kubeflownotebookswg/codeserver-python:{TAG}
     - code-server (Visual Studio Code) + Conda Python
   * - `rstudio-tidyverse <https://github.com/kubeflow/kubeflow/tree/master/components/example-notebook-servers/rstudio-tidyverse>`__
     - kubeflownotebookswg/rstudio-tidyverse:{TAG}
     - RStudio + `Tidyverse <https://www.tidyverse.org/>`_ packages

.. seealso::
   - `Arrikto Kubeflow Notebooks <https://docs.arrikto.com/features/notebook-images.html#>`_
   - `Get started with Charmed Kubeflow <https://charmed-kubeflow.io/docs/get-started-with-charmed-kubeflow#heading--kubeflow-notebooks>`_
   - `Kubeflow Notebooks <https://www.kubeflow.org/docs/components/notebooks/>`_
   - `Example Notebook Servers <https://github.com/kubeflow/kubeflow/tree/master/components/example-notebook-servers>`_
   - `Container Images <https://www.kubeflow.org/docs/components/notebooks/container-images/>`_
