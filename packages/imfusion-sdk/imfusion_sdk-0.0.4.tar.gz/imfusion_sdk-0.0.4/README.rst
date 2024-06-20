**Warning:**

| **This is only a placeholder package as we are restricted by PyPI's file size limit.**
| **To download the real package, use:**
| ``pip install imfusion-sdk --extra-index-url=https://pypi.imfusion.com``


**Disclaimer:**

Not for commercial use.

This python package is currently a public beta release.
You can use it free of charge for non-commercial applications until further notice.
To use it, you still require a (free) license key, which you can get from the `Python SDK product page <https://shop.imfusion.com/products/imfusion-python-sdk>`_.
For commercial applications, please get in touch with us at info@imfusion.com.

Note also, the functionality offered here is only a subset of the Python bindings we have available.
In particular, modality-specific plugins (e.g. for Ultrasound, CT, etc.) are not included.
Please reach out to us if you are interested in such functionality or visit our `webshop <https://shop.imfusion.com/>`_.

.. image:: https://www.imfusion.com/images/imfusion/imfusion_logo_hires.png
	:width: 500
	:align: center

Overview
========


Description
-----------

The ``imfusion`` package enables easy and fast loading, handling and processing of medical image data.
It is a wrapper around the ImFusion SDK and exposes a subset of its functionality to Python.
The major advantages of using ``imfusion`` are:

- **High Performance:**

	Leveraging optimized C++ for fast execution and OpenGL for GPU acceleration, ensuring compatibility with various GPU vendors.

- **Versatile Data Structures**:

	Handle a wide range of medical images and data types, including 2D/3D images, metadata, deformations, rotations, masks, and segmentations.
	It also supports keypoints, point clouds, and meshes.

- **Extensive Set of Algorithms:**

	Access a vast array of image processing algorithms, from basic cropping to complex multi-modal image registration.
	Even algorithms that don't have dedicated Python bindings can be executed through a functional interface.

- **File Format Support:**

	Load and save numerous medical imaging formats, including Nifti, MHD, Dicom, HDF5, PNG, and JPG and featuring a reliable Dicom loader used in FDA-approved products.

- **Deployment-Ready Data Pipelines:**

	Construct efficient data pipelines for ML model training and deployment, ensuring consistent pre-processing and post-processing.

- **numpy-like arithmetic but with images**

	Perform arithmetic operations on images with a functional API or operators, supporting GPU or CPU execution and, optionally, delayed expression evaluation for enhanced performance.

Documentation
-------------

Please find the documentation for this Python package at `docs.imfusion.com/python <https://docs.imfusion.com/python>`_.


Support
-------

If you experience issues with this package, please let us know in our `forum <https://forum.imfusion.com/c/python-sdk/>`_.

For business inquiries please contact info@imfusion.com.
