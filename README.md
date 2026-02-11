<!-- BEGIN_ANSIBLE_DOCS -->
<!--
Do not edit README.md directly!

This file is generated automatically by aar-doc and will be overwritten.

Please edit meta/argument_specs.yml instead.
-->
# ansible-proserver-kibana

kibana role for Proserver

## Supported Operating Systems

- Debian 12, 13
- Ubuntu 24.04, 22.04
- FreeBSD [Proserver](https://infrastructure.punkt.de/de/produkte/proserver.html)

## Role Arguments



#### Options for `kibana`

|Option|Description|Type|Required|Default|
|---|---|---|---|---|
| `use_dehydrated` | Whether to configure an SSL certificate and a reverse proxy for Kibana. If set to `true`, will use ansible-proserver-nginx and ansible-proserver-dehydrated to set up an Nginx-based reverse proxy with a valid SSL certificate that listens on 0.0.0.0:443. In order for this to work, `kibana.domain` has to be set to a valid, DNS-resolvable FQDN. Please consult the documentation of [ansible-proserver-dehydrated](https://github.com/punktDe/ansible-proserver-dehydrated) for available challenges. | bool | no | True |
| `domain` | Domain used for the Kibana reverse proxy (server_name and SSL certificate). Required when `kibana.use_dehydrated` is true. | str | no |  |
| `version` | The major version of Kibana to be configured/installed. When set to >= 8, the role applies systemd service overrides for the Kibana process and enables security settings by default. Please consult the documentation of [ansible-proserver-elasticsearch](https://github.com/punktDe/ansible-proserver-elasticsearch) for more information on the security settings.` | int | no | 8 |
| `prefix` | Sets folders/prefixes for Kibana directories. | dict of 'prefix' options | no |  |
| `repository` | Configuration options for the package repository used to install Kibana. | dict of 'repository' options | no |  |
| `oauth2_proxy` | Key of the`oauth2_proxy.config` dict to enable Identity-Aware Proxy (IAP) authentication for Kibana behind the reverse proxy. When set, the Nginx configuration will use auth_request to the corresponding oauth2_proxy instance (e.g. /proserver/iap). | str | no |  |
| `kibana.yml` | Allows to define options included in the kibana.yml file. Consult defaults/main.yaml for options set by default (path.data, xpack settings), and https://www.elastic.co/guide/en/kibana/current/settings.html for Kibana configuration reference. When Kibana version is >= 8, the keys apm, graph, ml, and reporting are removed from the rendered config as they are no longer supported. | dict | yes |  |

#### Options for `kibana.prefix`

|Option|Description|Type|Required|Default|
|---|---|---|---|---|
| `config` | Path for configuration files (e.g. kibana.yml). Defaults to /etc/kibana on Linux and /usr/local/etc/kibana on FreeBSD Proserver. | str | no |  |

#### Options for `kibana.repository`

|Option|Description|Type|Required|Default|
|---|---|---|---|---|
| `apt` | Configuration options for APT repository (only applies for Debian-based systems). | dict of 'apt' options | no |  |

#### Options for `kibana.repository.apt`

|Option|Description|Type|Required|Default|
|---|---|---|---|---|
| `key_url` |  | str | no | https://artifacts.elastic.co/GPG-KEY-elasticsearch |
| `repository` |  | str | no | https://artifacts.elastic.co/packages/{{ kibana.version }}.x/apt |

## Dependencies
- dehydrated
- nginx
- elasticsearch

## Installation
Add this role to the requirements.yml of your playbook as follows:
```yaml
roles:
  - name: ansible-proserver-kibana
    src: https://github.com/punktDe/ansible-proserver-kibana
```

Afterwards, install the role by running `ansible-galaxy install -r requirements.yml`

## Example Playbook

```yaml
- hosts: all
  roles:
    - name: kibana
```

<!-- END_ANSIBLE_DOCS -->
