Role Name
=========

Psuedo role to install and setup [Hybrid Cloud Platform](https://wiki.cisco.com/display/HCI/Cloud+Images) agents. This role is intended to  build platform images based on [Cloud9 images](https://wwwin-github.cisco.com/pages/sto-ccc/cloud9-docs/tools/#hardening-guides).

Requirements
------------

Any pre-requisites that may not be covered by Ansible itself or the role should be mentioned here. For instance, if the role uses the EC2 module, it may be a good idea to mention in this section that the boto package is required.

* yaml-lint
* ansible-lint
* molecule
* Docker
* AWS

Role Variables
--------------

A description of the settable variables for this role should go here, including any variables that are in defaults/main.yml, vars/main.yml, and any variables that can/should be set via parameters to the role. Any variables that are read from other roles and/or the global scope (ie. hostvars, group vars, etc.) should be mentioned here as well.

* Toggle installation of cloudwatch *cloudwatch_install: true*
* Specify version of cloudwatch rpm *cloudwatch_version: "latest"*


Dependencies
------------
* Python3 module dependencies are managed using 'pipenv'

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      tasks:
        - name: "Include hcplat_agents"
          include_role:
            name: "hcplat_agents"


Testing
-------

### Matrix
```
  Instance Name │ Driver Name │ Provisioner Name │ Scenario Name │ Created │ Converged
╶───────────────┼─────────────┼──────────────────┼───────────────┼─────────┼───────────╴
  Ubuntu        │ ec2         │ ansible          │ aws-ec2       │ false   │ false
  CentOS        │ ec2         │ ansible          │ aws-ec2       │ false   │ false
  CentOS        │ docker      │ ansible          │ default       │ false   │ false
  Ubuntu        │ docker      │ ansible          │ default       │ false   │ false

```

### To test against local docker instance of Ubuntu & CentOS images
``` 
pipenv shell --python 3.9
pipenv install --skip-lock
pipenv run molecule converge
pipenv run molecule verify
pipenv run molecule destroy
```

### TODO: To test against AWS ec2 instances
```
EXPORT AWS_REGION=us-east-1
pipenv shell --python 3.9
pipenv install --skip-lock
pipenv run molecule create -s aws-ec2
pipenv run molecule converge -s aws-ec2
pipenv run molecule verify -s aws-ec2
pipenv run molecule destroy -s aws-ec2
```

License
-------

BSD

Author Information
------------------

An optional section for the role authors to include contact information, or a website (HTML is not allowed).
