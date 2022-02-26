# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from . import _utilities
import typing
# Export this package's modules as members:
from .domain import *
from .domain_credential import *
from .get_domain import *
from .provider import *
from .route import *
from ._inputs import *
from . import outputs

# Make subpackages available:
if typing.TYPE_CHECKING:
    import pulumi_mailgun.config as __config
    config = __config
else:
    config = _utilities.lazy_import('pulumi_mailgun.config')

_utilities.register(
    resource_modules="""
[
 {
  "pkg": "mailgun",
  "mod": "index/domain",
  "fqn": "pulumi_mailgun",
  "classes": {
   "mailgun:index/domain:Domain": "Domain"
  }
 },
 {
  "pkg": "mailgun",
  "mod": "index/domainCredential",
  "fqn": "pulumi_mailgun",
  "classes": {
   "mailgun:index/domainCredential:DomainCredential": "DomainCredential"
  }
 },
 {
  "pkg": "mailgun",
  "mod": "index/route",
  "fqn": "pulumi_mailgun",
  "classes": {
   "mailgun:index/route:Route": "Route"
  }
 }
]
""",
    resource_packages="""
[
 {
  "pkg": "mailgun",
  "token": "pulumi:providers:mailgun",
  "fqn": "pulumi_mailgun",
  "class": "Provider"
 }
]
"""
)
