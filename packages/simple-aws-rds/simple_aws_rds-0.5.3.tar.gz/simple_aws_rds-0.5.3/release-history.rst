.. _release_history:

Release and Version History
==============================================================================


Backlog (TODO)
------------------------------------------------------------------------------
**Features and Improvements**

- add ``RDSDBCluster``

**Minor Improvements**

**Bugfixes**

**Miscellaneous**


0.5.3 (2024-06-19)
------------------------------------------------------------------------------
**Minor Improvements**

- Now ``RDSDBInstance.status`` attribute is optional.

**Bugfixes**

- fix a bug that ``RDSDBSnapshot.wait_for_status`` uses the wrong status enum class.


0.5.2 (2024-06-18)
------------------------------------------------------------------------------
**Bugfixes**

- Fix a bug that waiter method does not respect ``gap`` and ``instant`` parameter.


0.5.1 (2024-06-18)
------------------------------------------------------------------------------
**Features and Improvements**

- add ``RDSDBSnapshot``

**Minor Improvements**

- the waiter method now can do the check instantly.
- add document website.


0.4.1 (2023-06-19)
------------------------------------------------------------------------------
**Features and Improvements**

- add ``RDSDBInstance.delete_db_instance``


0.3.1 (2023-06-15)
------------------------------------------------------------------------------
**Features and Improvements**

- add ``RDSDBInstanceStatusGroupEnum``
- add ``RDSDBInstance.wait_for_available``
- add ``RDSDBInstance.wait_for_stopped``


0.2.1 (2023-06-15)
------------------------------------------------------------------------------
**Features and Improvements**

- add ``RDSDBInstnace.wait_for_status`` method

**Minor Improvements**

- add a lot more attributes to ``RDSDBInstnace``
- add a lot more status enum to ``RDSDBInstanceStatusEnum``


0.1.2 (2023-05-03)
------------------------------------------------------------------------------
**Bugfixes**

- fix a bug that when you describe db instances with db identifier, we should not use any paginator configuration.


0.1.1 (2023-05-03)
------------------------------------------------------------------------------
**Features and Improvements**

- First release
- Add ``RDSDBInstnace``
