.. _sec-user_guide-install:

Installation
============

.. warning::

   Windows support is currently experimental. Please report issues on our
   `issue tracker <https://github.com/eradiate/eradiate/issues>`_.

Eradiate is delivered through PyPI and can be installed using the ``pip``. This
is the recommended way to install Eradiate.

.. code:: bash

   pip install eradiate

This will install the latest stable version of Eradiate, along with all the
dependencies necessary to run it. If you want to install the latest development
version, please refer to the :ref:`sec-developer_guide-dev_install`.

.. warning::

   Eradiate uses a modified version of the Mitsuba 3 renderer, distributed on
   PyPI as ``eradiate-mitsuba``. That package conflicts with the ``mitsuba``
   package distributed by the Mitsuba team and both cannot be installed
   together.

   The ``eradiate`` PyPI package lists ``eradiate-mitsuba`` as a dependency. A
   normal usage pattern should result in the correct flavour of Mitsuba being
   installed automatically. However, if you are installing Eradiate to an
   environment already containing a Mitsuba installation, be sure to remove it
   before installing Eradiate.

After installing Eradiate, it is recommended to download some support data to
start simulations:

.. code:: bash

   eradiate data fetch minimal

.. warning::

   Since v0.27.0, molecular absorption databases are no longer downloaded lazily
   when used for the first time. Instead, they must be downloaded prior to
   running Eradiate. See the :doc:`data guide </rst/data/intro>` for more
   information.
