Pacifica Travis CI
==================

This Ansible role defines configuration for deploying Pacifica services in an
Ansible managed infrastructure in Travis CI.

Requirements
------------

There are no requirements for this role currently. However, the Pacifica
services do depend on other services depending on configuration. So, please
be aware if you configure a service to use PostgreSQL you should configure
PostgreSQL prior to including this role as part of your deployment.

Role Variables
--------------

The role variables are to install Python on the different distributions. This
can be overridden by setting the `setup_packages` and `python_packages` to
a list of custom packages in a `default.yml` in a consuming role.
Alternatively, if the consuming playbook is installing python by other means,
you can set `external_python` to any value and the python installation task
will be skipped.

The other role variables are default configurations for the different Pacifica
services. Each Pacifica service has different configuration requirements. These
configuration requirements are consistent between services and can be configured
the same way across services. For example, both the `ingest` and `metadata`
services require databases and those are managed by the same interface. However,
the `ingest` process requires a Celery backend where the `metadata` does not.

Role Defaults
--------------

The role defaults are there to control the user driven configuration of the
Pacifica services. Each service configuration should be a dictionary named 
in the `pacifica_available_services` dictionary. The service configurations
are then referenced by items in the `pacifica_enabled_services` list.

Dependencies
------------

There are currently no dependencies for this role. However, if you configure a
Pacifica service to use a MySQL or PostgreSQL database to store its state then
you are responsible for making sure that MySQL or PostgreSQL service is deployed
and configured somewhere in your infrastructure. This includes other optional
dependencies like ElasticSearch.

Example Playbook
----------------

Including the role is similar to other ansible roles. There are examples of this
in the `molecule` subdirectory for picking out specific services to deploy on
specific systems.

Simple Example:
```
    - hosts: servers
      roles:
         - role: pacifica
           pacifica_enabled_services:
             - metadata
             - policy
```

License
-------

LGPLv3

Author Information
------------------

Pacifica is a community lead effort and supporting these services are handled by the
Ansible team. Some of those members are referenced below.

 * David Brown <dmlb2000@gmail.com>: Primary Pacifica Architect
 * Ian Smith <gitbytes@gmail.com>: Community Contributor
