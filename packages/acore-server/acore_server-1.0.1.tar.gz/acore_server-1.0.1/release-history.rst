.. _release_history:

Release and Version History
==============================================================================


x.y.z (Backlog)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

**Minor Improvements**

**Bugfixes**

**Miscellaneous**


1.0.1 (2024-06-20)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**💥Breaking Changes**

- Moved most of server operation logics into this library.

**Features and Improvements**

- Add lot of `workflows <https://acore-server.readthedocs.io/en/latest/search.html?q=Operation+and+Workflow&check_keywords=yes&area=default>`_.


0.2.5 (2023-07-18)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

**Minor Improvements**

- add ``acore_db_app_version`` argument to ``acore_server.fleet.Server.run_ec2`` method.

**Bugfixes**

**Miscellaneous**


0.2.4 (2023-06-28)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Miscellaneous**

- Upgrade ``acore_server_config`` dependency from 0.4.2 to 0.5.1.


0.2.3 (2023-06-28)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Miscellaneous**

- Upgrade dependencies.


0.2.2 (2023-06-28)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Miscellaneous**

- Remove unnecessary dependencies.


0.2.1 (2023-06-27)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

- Add ``acore_server.api.Server.from_ec2_inside``


0.1.2 (2023-06-27)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Minor Improvements**

- Add ``acore_soap_app_version``, ``acore_server_bootstrap_version`` arguments to ``acore_server.api.Server.bootstrap`` method.
- Add ``acore_server.api.Server.stop_check_server_status_cron_job``.

**Bugfixes**

- Fix some but that some remote command should be run as ubuntu user, not root.

**Miscellaneous**

- Upgrade dependencies.


0.1.1 (2023-06-27)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

- First release
- Add the following public API:
    - ``acore_server.api.Server``
    - ``acore_server.api.Fleet``
    - ``acore_server.api.InfraStackExports``
