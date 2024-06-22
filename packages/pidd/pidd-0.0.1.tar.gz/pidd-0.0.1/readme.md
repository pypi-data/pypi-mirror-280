# Python Integration, Delivery & Deployment

Get a common set of Python CI & CD commands \
from various contexts of CA, CI and OCI / OS.

## Features

* [X] CA certificates
  * [X] custom
  * [X] known
* [ ] Continuous Integration platforms
  * [X] ForgeJo
  * [X] Gitea
  * [X] GitHub
  * [X] GitLab
  * [ ] SourceHut
* [X] Operating Systems
  * [X] Alma → Python 3.11
    * [X] 8
    * [X] 9
  * [X] Alpine → Python 3.11
    * [X] 3.18
    * [X] 3.19
  * [ ] Arch → Python 3.12
    * [ ] 20231112
    * [X] 20240101
  * [ ] Debian
    * [ ] Bullseye (11) → Python 3.9
    * [X] Bookworm (12) → Python 3.11
  * [X] Fedora → Python 3.12
    * [X] 39
    * [X] 40
  * [X] Rocky → Python 3.11
    * [X] 8
    * [X] 9
  * [X] Ubuntu
    * [X] Jammy (22.04) → Python 3.10
    * [X] Noble (24.04) → Python 3.12

## How

| Variable        | Description             | Default                         |
|:----------------|:------------------------|:--------------------------------|
| PIDD_CA_n       | Numbered CA certificate |                                 |
| PIDD_DNS        | Space separated servers | 9.9.9.9                         |
| PIDD_GIT_CHILD  | Child Git repository    | pidd                            |
| PIDD_GIT_PARENT | Parent Git repository   | rwx                             |
| PIDD_SSH_HOSTS  | domain.tld ssh-type pub |                                 |
| PIDD_SSH_KEY    | SSH private key         |                                 |
| PIDD_URL_ALMA   | Alma repository URL     | https://repo.almalinux.org      |
| PIDD_URL_ALPINE | Alpine repository URL   | https://dl-cdn.alpinelinux.org  |
| PIDD_URL_ARCH   | Arch repository URL     | https://geo.mirror.pkgbuild.com |
| PIDD_URL_DEBIAN | Debian repository URL   | https://deb.debian.org          |
| PIDD_URL_FEDORA | Fedora repository URL   | https://rpmfind.net             |
| PIDD_URL_ROCKY  | Rocky repository URL    | https://dl.rockylinux.org       |
| PIDD_URL_UBUNTU | Ubuntu repository URL   | https://ubuntu.mirrors.ovh.net  |

## HTTPS & Python

| OS img  | crt | upd | Python |
|:--------|-----|-----|:-------|
| Alma 8  | ☑   | ☑   | ☐      |
| Alma 9  | ☑   | ☑   | ☑ 3.9  |
| Alpine  | ☑   | ☐   | ☐      |
| Arch    | ☑   | ☑   | ☐      |
| Debian  | ☐   | ☐   | ☐      |
| Fedora  | ☑   | ☑   | ☑ 3.12 |
| Rocky 8 | ☑   | ☑   | ☐      |
| Rocky 9 | ☑   | ☑   | ☑ 3.9  |
| Ubuntu  | ☐   | ☐   | ☐      |

## Tasks

* relay environment module name
* show previous states of directories & files
* write tests

### .py

* detect ssh private key type
* implement project repository cloning
* install
  * epel
    * shellcheck
  * openssh
  * pip
    * ruff
  * rsync
* lint
  * .py
  * .sh
* write bootstrap entry point

### .sh

* handle git cloning credentials
* override repository and framework locations
* reduce single conditions with &&
* support opensuse
