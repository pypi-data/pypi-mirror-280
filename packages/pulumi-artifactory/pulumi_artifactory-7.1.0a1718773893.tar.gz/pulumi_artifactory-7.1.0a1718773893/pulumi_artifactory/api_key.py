# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['ApiKeyArgs', 'ApiKey']

@pulumi.input_type
class ApiKeyArgs:
    def __init__(__self__):
        """
        The set of arguments for constructing a ApiKey resource.
        """
        pass


@pulumi.input_type
class _ApiKeyState:
    def __init__(__self__, *,
                 api_key: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering ApiKey resources.
        :param pulumi.Input[str] api_key: The API key. Deprecated.
        """
        if api_key is not None:
            warnings.warn("""Deprecated in favor of \"ScopedToken\".""", DeprecationWarning)
            pulumi.log.warn("""api_key is deprecated: Deprecated in favor of \"ScopedToken\".""")
        if api_key is not None:
            pulumi.set(__self__, "api_key", api_key)

    @property
    @pulumi.getter(name="apiKey")
    def api_key(self) -> Optional[pulumi.Input[str]]:
        """
        The API key. Deprecated.
        """
        warnings.warn("""Deprecated in favor of \"ScopedToken\".""", DeprecationWarning)
        pulumi.log.warn("""api_key is deprecated: Deprecated in favor of \"ScopedToken\".""")

        return pulumi.get(self, "api_key")

    @api_key.setter
    def api_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "api_key", value)


class ApiKey(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 __props__=None):
        """
        Provides an Artifactory API key resource. This can be used to create and manage Artifactory API keys.

        > **Note:** API keys will be stored in the raw state as plain-text. Read more about sensitive data in state.

        !> As notified in [Artifactory 7.47.10](https://jfrog.com/help/r/jfrog-release-information/artifactory-7.47.10-cloud-self-hosted), support for API Key is slated to be removed in a future release. To ease customer migration to [reference tokens](https://jfrog.com/help/r/jfrog-platform-administration-documentation/user-profile), which replaces API key, we are disabling the ability to create new API keys at the end of Q3 2024. The ability to use API keys will be removed at the end of Q4 2024. For more information, see [JFrog API Key Deprecation Process](https://jfrog.com/help/r/jfrog-platform-administration-documentation/jfrog-api-key-deprecation-process).

        ## Example Usage

        ```python
        import pulumi
        import pulumi_artifactory as artifactory

        # Create a new Artifactory API key for the configured user
        ci = artifactory.ApiKey("ci")
        ```

        ## Import

        A user's API key can be imported using any identifier, e.g.

        ```sh
        $ pulumi import artifactory:index/apiKey:ApiKey test import
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[ApiKeyArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides an Artifactory API key resource. This can be used to create and manage Artifactory API keys.

        > **Note:** API keys will be stored in the raw state as plain-text. Read more about sensitive data in state.

        !> As notified in [Artifactory 7.47.10](https://jfrog.com/help/r/jfrog-release-information/artifactory-7.47.10-cloud-self-hosted), support for API Key is slated to be removed in a future release. To ease customer migration to [reference tokens](https://jfrog.com/help/r/jfrog-platform-administration-documentation/user-profile), which replaces API key, we are disabling the ability to create new API keys at the end of Q3 2024. The ability to use API keys will be removed at the end of Q4 2024. For more information, see [JFrog API Key Deprecation Process](https://jfrog.com/help/r/jfrog-platform-administration-documentation/jfrog-api-key-deprecation-process).

        ## Example Usage

        ```python
        import pulumi
        import pulumi_artifactory as artifactory

        # Create a new Artifactory API key for the configured user
        ci = artifactory.ApiKey("ci")
        ```

        ## Import

        A user's API key can be imported using any identifier, e.g.

        ```sh
        $ pulumi import artifactory:index/apiKey:ApiKey test import
        ```

        :param str resource_name: The name of the resource.
        :param ApiKeyArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ApiKeyArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ApiKeyArgs.__new__(ApiKeyArgs)

            __props__.__dict__["api_key"] = None
        secret_opts = pulumi.ResourceOptions(additional_secret_outputs=["apiKey"])
        opts = pulumi.ResourceOptions.merge(opts, secret_opts)
        super(ApiKey, __self__).__init__(
            'artifactory:index/apiKey:ApiKey',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            api_key: Optional[pulumi.Input[str]] = None) -> 'ApiKey':
        """
        Get an existing ApiKey resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] api_key: The API key. Deprecated.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ApiKeyState.__new__(_ApiKeyState)

        __props__.__dict__["api_key"] = api_key
        return ApiKey(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="apiKey")
    def api_key(self) -> pulumi.Output[str]:
        """
        The API key. Deprecated.
        """
        warnings.warn("""Deprecated in favor of \"ScopedToken\".""", DeprecationWarning)
        pulumi.log.warn("""api_key is deprecated: Deprecated in favor of \"ScopedToken\".""")

        return pulumi.get(self, "api_key")

