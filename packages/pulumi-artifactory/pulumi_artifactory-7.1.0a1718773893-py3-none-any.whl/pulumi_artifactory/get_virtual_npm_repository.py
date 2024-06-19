# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = [
    'GetVirtualNpmRepositoryResult',
    'AwaitableGetVirtualNpmRepositoryResult',
    'get_virtual_npm_repository',
    'get_virtual_npm_repository_output',
]

@pulumi.output_type
class GetVirtualNpmRepositoryResult:
    """
    A collection of values returned by getVirtualNpmRepository.
    """
    def __init__(__self__, artifactory_requests_can_retrieve_remote_artifacts=None, default_deployment_repo=None, description=None, excludes_pattern=None, external_dependencies_enabled=None, external_dependencies_patterns=None, external_dependencies_remote_repo=None, id=None, includes_pattern=None, key=None, notes=None, package_type=None, project_environments=None, project_key=None, repo_layout_ref=None, repositories=None, retrieval_cache_period_seconds=None):
        if artifactory_requests_can_retrieve_remote_artifacts and not isinstance(artifactory_requests_can_retrieve_remote_artifacts, bool):
            raise TypeError("Expected argument 'artifactory_requests_can_retrieve_remote_artifacts' to be a bool")
        pulumi.set(__self__, "artifactory_requests_can_retrieve_remote_artifacts", artifactory_requests_can_retrieve_remote_artifacts)
        if default_deployment_repo and not isinstance(default_deployment_repo, str):
            raise TypeError("Expected argument 'default_deployment_repo' to be a str")
        pulumi.set(__self__, "default_deployment_repo", default_deployment_repo)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if excludes_pattern and not isinstance(excludes_pattern, str):
            raise TypeError("Expected argument 'excludes_pattern' to be a str")
        pulumi.set(__self__, "excludes_pattern", excludes_pattern)
        if external_dependencies_enabled and not isinstance(external_dependencies_enabled, bool):
            raise TypeError("Expected argument 'external_dependencies_enabled' to be a bool")
        pulumi.set(__self__, "external_dependencies_enabled", external_dependencies_enabled)
        if external_dependencies_patterns and not isinstance(external_dependencies_patterns, list):
            raise TypeError("Expected argument 'external_dependencies_patterns' to be a list")
        pulumi.set(__self__, "external_dependencies_patterns", external_dependencies_patterns)
        if external_dependencies_remote_repo and not isinstance(external_dependencies_remote_repo, str):
            raise TypeError("Expected argument 'external_dependencies_remote_repo' to be a str")
        pulumi.set(__self__, "external_dependencies_remote_repo", external_dependencies_remote_repo)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if includes_pattern and not isinstance(includes_pattern, str):
            raise TypeError("Expected argument 'includes_pattern' to be a str")
        pulumi.set(__self__, "includes_pattern", includes_pattern)
        if key and not isinstance(key, str):
            raise TypeError("Expected argument 'key' to be a str")
        pulumi.set(__self__, "key", key)
        if notes and not isinstance(notes, str):
            raise TypeError("Expected argument 'notes' to be a str")
        pulumi.set(__self__, "notes", notes)
        if package_type and not isinstance(package_type, str):
            raise TypeError("Expected argument 'package_type' to be a str")
        pulumi.set(__self__, "package_type", package_type)
        if project_environments and not isinstance(project_environments, list):
            raise TypeError("Expected argument 'project_environments' to be a list")
        pulumi.set(__self__, "project_environments", project_environments)
        if project_key and not isinstance(project_key, str):
            raise TypeError("Expected argument 'project_key' to be a str")
        pulumi.set(__self__, "project_key", project_key)
        if repo_layout_ref and not isinstance(repo_layout_ref, str):
            raise TypeError("Expected argument 'repo_layout_ref' to be a str")
        pulumi.set(__self__, "repo_layout_ref", repo_layout_ref)
        if repositories and not isinstance(repositories, list):
            raise TypeError("Expected argument 'repositories' to be a list")
        pulumi.set(__self__, "repositories", repositories)
        if retrieval_cache_period_seconds and not isinstance(retrieval_cache_period_seconds, int):
            raise TypeError("Expected argument 'retrieval_cache_period_seconds' to be a int")
        pulumi.set(__self__, "retrieval_cache_period_seconds", retrieval_cache_period_seconds)

    @property
    @pulumi.getter(name="artifactoryRequestsCanRetrieveRemoteArtifacts")
    def artifactory_requests_can_retrieve_remote_artifacts(self) -> Optional[bool]:
        return pulumi.get(self, "artifactory_requests_can_retrieve_remote_artifacts")

    @property
    @pulumi.getter(name="defaultDeploymentRepo")
    def default_deployment_repo(self) -> Optional[str]:
        return pulumi.get(self, "default_deployment_repo")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="excludesPattern")
    def excludes_pattern(self) -> Optional[str]:
        return pulumi.get(self, "excludes_pattern")

    @property
    @pulumi.getter(name="externalDependenciesEnabled")
    def external_dependencies_enabled(self) -> Optional[bool]:
        return pulumi.get(self, "external_dependencies_enabled")

    @property
    @pulumi.getter(name="externalDependenciesPatterns")
    def external_dependencies_patterns(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "external_dependencies_patterns")

    @property
    @pulumi.getter(name="externalDependenciesRemoteRepo")
    def external_dependencies_remote_repo(self) -> Optional[str]:
        return pulumi.get(self, "external_dependencies_remote_repo")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="includesPattern")
    def includes_pattern(self) -> Optional[str]:
        return pulumi.get(self, "includes_pattern")

    @property
    @pulumi.getter
    def key(self) -> str:
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def notes(self) -> Optional[str]:
        return pulumi.get(self, "notes")

    @property
    @pulumi.getter(name="packageType")
    def package_type(self) -> str:
        return pulumi.get(self, "package_type")

    @property
    @pulumi.getter(name="projectEnvironments")
    def project_environments(self) -> Sequence[str]:
        return pulumi.get(self, "project_environments")

    @property
    @pulumi.getter(name="projectKey")
    def project_key(self) -> Optional[str]:
        return pulumi.get(self, "project_key")

    @property
    @pulumi.getter(name="repoLayoutRef")
    def repo_layout_ref(self) -> Optional[str]:
        return pulumi.get(self, "repo_layout_ref")

    @property
    @pulumi.getter
    def repositories(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "repositories")

    @property
    @pulumi.getter(name="retrievalCachePeriodSeconds")
    def retrieval_cache_period_seconds(self) -> Optional[int]:
        """
        (Optional, Default: `7200`) This value refers to the number of seconds to cache metadata files before checking for newer versions on aggregated repositories. A value of 0 indicates no caching.
        """
        return pulumi.get(self, "retrieval_cache_period_seconds")


class AwaitableGetVirtualNpmRepositoryResult(GetVirtualNpmRepositoryResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetVirtualNpmRepositoryResult(
            artifactory_requests_can_retrieve_remote_artifacts=self.artifactory_requests_can_retrieve_remote_artifacts,
            default_deployment_repo=self.default_deployment_repo,
            description=self.description,
            excludes_pattern=self.excludes_pattern,
            external_dependencies_enabled=self.external_dependencies_enabled,
            external_dependencies_patterns=self.external_dependencies_patterns,
            external_dependencies_remote_repo=self.external_dependencies_remote_repo,
            id=self.id,
            includes_pattern=self.includes_pattern,
            key=self.key,
            notes=self.notes,
            package_type=self.package_type,
            project_environments=self.project_environments,
            project_key=self.project_key,
            repo_layout_ref=self.repo_layout_ref,
            repositories=self.repositories,
            retrieval_cache_period_seconds=self.retrieval_cache_period_seconds)


def get_virtual_npm_repository(artifactory_requests_can_retrieve_remote_artifacts: Optional[bool] = None,
                               default_deployment_repo: Optional[str] = None,
                               description: Optional[str] = None,
                               excludes_pattern: Optional[str] = None,
                               external_dependencies_enabled: Optional[bool] = None,
                               external_dependencies_patterns: Optional[Sequence[str]] = None,
                               external_dependencies_remote_repo: Optional[str] = None,
                               includes_pattern: Optional[str] = None,
                               key: Optional[str] = None,
                               notes: Optional[str] = None,
                               project_environments: Optional[Sequence[str]] = None,
                               project_key: Optional[str] = None,
                               repo_layout_ref: Optional[str] = None,
                               repositories: Optional[Sequence[str]] = None,
                               retrieval_cache_period_seconds: Optional[int] = None,
                               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetVirtualNpmRepositoryResult:
    """
    Retrieves a virtual NPM repository.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_artifactory as artifactory

    virtual_npm = artifactory.get_virtual_npm_repository(key="virtual-npm")
    ```


    :param str key: the identity key of the repo.
    :param int retrieval_cache_period_seconds: (Optional, Default: `7200`) This value refers to the number of seconds to cache metadata files before checking for newer versions on aggregated repositories. A value of 0 indicates no caching.
    """
    __args__ = dict()
    __args__['artifactoryRequestsCanRetrieveRemoteArtifacts'] = artifactory_requests_can_retrieve_remote_artifacts
    __args__['defaultDeploymentRepo'] = default_deployment_repo
    __args__['description'] = description
    __args__['excludesPattern'] = excludes_pattern
    __args__['externalDependenciesEnabled'] = external_dependencies_enabled
    __args__['externalDependenciesPatterns'] = external_dependencies_patterns
    __args__['externalDependenciesRemoteRepo'] = external_dependencies_remote_repo
    __args__['includesPattern'] = includes_pattern
    __args__['key'] = key
    __args__['notes'] = notes
    __args__['projectEnvironments'] = project_environments
    __args__['projectKey'] = project_key
    __args__['repoLayoutRef'] = repo_layout_ref
    __args__['repositories'] = repositories
    __args__['retrievalCachePeriodSeconds'] = retrieval_cache_period_seconds
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('artifactory:index/getVirtualNpmRepository:getVirtualNpmRepository', __args__, opts=opts, typ=GetVirtualNpmRepositoryResult).value

    return AwaitableGetVirtualNpmRepositoryResult(
        artifactory_requests_can_retrieve_remote_artifacts=pulumi.get(__ret__, 'artifactory_requests_can_retrieve_remote_artifacts'),
        default_deployment_repo=pulumi.get(__ret__, 'default_deployment_repo'),
        description=pulumi.get(__ret__, 'description'),
        excludes_pattern=pulumi.get(__ret__, 'excludes_pattern'),
        external_dependencies_enabled=pulumi.get(__ret__, 'external_dependencies_enabled'),
        external_dependencies_patterns=pulumi.get(__ret__, 'external_dependencies_patterns'),
        external_dependencies_remote_repo=pulumi.get(__ret__, 'external_dependencies_remote_repo'),
        id=pulumi.get(__ret__, 'id'),
        includes_pattern=pulumi.get(__ret__, 'includes_pattern'),
        key=pulumi.get(__ret__, 'key'),
        notes=pulumi.get(__ret__, 'notes'),
        package_type=pulumi.get(__ret__, 'package_type'),
        project_environments=pulumi.get(__ret__, 'project_environments'),
        project_key=pulumi.get(__ret__, 'project_key'),
        repo_layout_ref=pulumi.get(__ret__, 'repo_layout_ref'),
        repositories=pulumi.get(__ret__, 'repositories'),
        retrieval_cache_period_seconds=pulumi.get(__ret__, 'retrieval_cache_period_seconds'))


@_utilities.lift_output_func(get_virtual_npm_repository)
def get_virtual_npm_repository_output(artifactory_requests_can_retrieve_remote_artifacts: Optional[pulumi.Input[Optional[bool]]] = None,
                                      default_deployment_repo: Optional[pulumi.Input[Optional[str]]] = None,
                                      description: Optional[pulumi.Input[Optional[str]]] = None,
                                      excludes_pattern: Optional[pulumi.Input[Optional[str]]] = None,
                                      external_dependencies_enabled: Optional[pulumi.Input[Optional[bool]]] = None,
                                      external_dependencies_patterns: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                                      external_dependencies_remote_repo: Optional[pulumi.Input[Optional[str]]] = None,
                                      includes_pattern: Optional[pulumi.Input[Optional[str]]] = None,
                                      key: Optional[pulumi.Input[str]] = None,
                                      notes: Optional[pulumi.Input[Optional[str]]] = None,
                                      project_environments: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                                      project_key: Optional[pulumi.Input[Optional[str]]] = None,
                                      repo_layout_ref: Optional[pulumi.Input[Optional[str]]] = None,
                                      repositories: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                                      retrieval_cache_period_seconds: Optional[pulumi.Input[Optional[int]]] = None,
                                      opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetVirtualNpmRepositoryResult]:
    """
    Retrieves a virtual NPM repository.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_artifactory as artifactory

    virtual_npm = artifactory.get_virtual_npm_repository(key="virtual-npm")
    ```


    :param str key: the identity key of the repo.
    :param int retrieval_cache_period_seconds: (Optional, Default: `7200`) This value refers to the number of seconds to cache metadata files before checking for newer versions on aggregated repositories. A value of 0 indicates no caching.
    """
    ...
