# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_waf_openapi20211001 import models as waf_openapi_20211001_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_openapi_util.client import Client as OpenApiUtilClient


class Client(OpenApiClient):
    """
    *\
    """
    def __init__(
        self, 
        config: open_api_models.Config,
    ):
        super().__init__(config)
        self._endpoint_rule = 'regional'
        self._endpoint_map = {
            'cn-qingdao': 'wafopenapi.cn-hangzhou.aliyuncs.com',
            'cn-beijing': 'wafopenapi.cn-hangzhou.aliyuncs.com',
            'cn-chengdu': 'wafopenapi.cn-hangzhou.aliyuncs.com',
            'cn-zhangjiakou': 'wafopenapi.cn-hangzhou.aliyuncs.com',
            'cn-huhehaote': 'wafopenapi.cn-hangzhou.aliyuncs.com',
            'cn-hangzhou': 'wafopenapi.cn-hangzhou.aliyuncs.com',
            'cn-shanghai': 'wafopenapi.cn-hangzhou.aliyuncs.com',
            'cn-shenzhen': 'wafopenapi.cn-hangzhou.aliyuncs.com',
            'cn-heyuan': 'wafopenapi.cn-hangzhou.aliyuncs.com',
            'cn-wulanchabu': 'wafopenapi.cn-hangzhou.aliyuncs.com',
            'cn-hongkong': 'wafopenapi.ap-southeast-1.aliyuncs.com',
            'ap-southeast-1': 'wafopenapi.ap-southeast-1.aliyuncs.com',
            'ap-southeast-2': 'wafopenapi.ap-southeast-1.aliyuncs.com',
            'ap-southeast-3': 'wafopenapi.ap-southeast-1.aliyuncs.com',
            'ap-southeast-5': 'wafopenapi.ap-southeast-1.aliyuncs.com',
            'eu-west-1': 'wafopenapi.ap-southeast-1.aliyuncs.com',
            'us-west-1': 'wafopenapi.ap-southeast-1.aliyuncs.com',
            'us-east-1': 'wafopenapi.ap-southeast-1.aliyuncs.com',
            'eu-central-1': 'wafopenapi.ap-southeast-1.aliyuncs.com',
            'me-east-1': 'wafopenapi.ap-southeast-1.aliyuncs.com',
            'ap-south-1': 'wafopenapi.ap-southeast-1.aliyuncs.com',
            'cn-shanghai-finance-1': 'wafopenapi.cn-hangzhou.aliyuncs.com',
            'cn-shenzhen-finance-1': 'wafopenapi.cn-hangzhou.aliyuncs.com',
            'cn-north-2-gov-1': 'wafopenapi.cn-hangzhou.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('waf-openapi', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(
        self,
        product_id: str,
        region_id: str,
        endpoint_rule: str,
        network: str,
        suffix: str,
        endpoint_map: Dict[str, str],
        endpoint: str,
    ) -> str:
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def clear_major_protection_black_ip_with_options(
        self,
        request: waf_openapi_20211001_models.ClearMajorProtectionBlackIpRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.ClearMajorProtectionBlackIpResponse:
        """
        @summary Clears an IP address blacklist for major event protection.
        
        @param request: ClearMajorProtectionBlackIpRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ClearMajorProtectionBlackIpResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ClearMajorProtectionBlackIp',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.ClearMajorProtectionBlackIpResponse(),
            self.call_api(params, req, runtime)
        )

    async def clear_major_protection_black_ip_with_options_async(
        self,
        request: waf_openapi_20211001_models.ClearMajorProtectionBlackIpRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.ClearMajorProtectionBlackIpResponse:
        """
        @summary Clears an IP address blacklist for major event protection.
        
        @param request: ClearMajorProtectionBlackIpRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ClearMajorProtectionBlackIpResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ClearMajorProtectionBlackIp',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.ClearMajorProtectionBlackIpResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def clear_major_protection_black_ip(
        self,
        request: waf_openapi_20211001_models.ClearMajorProtectionBlackIpRequest,
    ) -> waf_openapi_20211001_models.ClearMajorProtectionBlackIpResponse:
        """
        @summary Clears an IP address blacklist for major event protection.
        
        @param request: ClearMajorProtectionBlackIpRequest
        @return: ClearMajorProtectionBlackIpResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.clear_major_protection_black_ip_with_options(request, runtime)

    async def clear_major_protection_black_ip_async(
        self,
        request: waf_openapi_20211001_models.ClearMajorProtectionBlackIpRequest,
    ) -> waf_openapi_20211001_models.ClearMajorProtectionBlackIpResponse:
        """
        @summary Clears an IP address blacklist for major event protection.
        
        @param request: ClearMajorProtectionBlackIpRequest
        @return: ClearMajorProtectionBlackIpResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.clear_major_protection_black_ip_with_options_async(request, runtime)

    def copy_defense_template_with_options(
        self,
        request: waf_openapi_20211001_models.CopyDefenseTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.CopyDefenseTemplateResponse:
        """
        @summary Creates a new protection template from the copy.
        
        @param request: CopyDefenseTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CopyDefenseTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CopyDefenseTemplate',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.CopyDefenseTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def copy_defense_template_with_options_async(
        self,
        request: waf_openapi_20211001_models.CopyDefenseTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.CopyDefenseTemplateResponse:
        """
        @summary Creates a new protection template from the copy.
        
        @param request: CopyDefenseTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CopyDefenseTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CopyDefenseTemplate',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.CopyDefenseTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def copy_defense_template(
        self,
        request: waf_openapi_20211001_models.CopyDefenseTemplateRequest,
    ) -> waf_openapi_20211001_models.CopyDefenseTemplateResponse:
        """
        @summary Creates a new protection template from the copy.
        
        @param request: CopyDefenseTemplateRequest
        @return: CopyDefenseTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.copy_defense_template_with_options(request, runtime)

    async def copy_defense_template_async(
        self,
        request: waf_openapi_20211001_models.CopyDefenseTemplateRequest,
    ) -> waf_openapi_20211001_models.CopyDefenseTemplateResponse:
        """
        @summary Creates a new protection template from the copy.
        
        @param request: CopyDefenseTemplateRequest
        @return: CopyDefenseTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.copy_defense_template_with_options_async(request, runtime)

    def create_defense_resource_group_with_options(
        self,
        request: waf_openapi_20211001_models.CreateDefenseResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.CreateDefenseResourceGroupResponse:
        """
        @summary Creates a protected object group.
        
        @param request: CreateDefenseResourceGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDefenseResourceGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.add_list):
            query['AddList'] = request.add_list
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDefenseResourceGroup',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.CreateDefenseResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_defense_resource_group_with_options_async(
        self,
        request: waf_openapi_20211001_models.CreateDefenseResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.CreateDefenseResourceGroupResponse:
        """
        @summary Creates a protected object group.
        
        @param request: CreateDefenseResourceGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDefenseResourceGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.add_list):
            query['AddList'] = request.add_list
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDefenseResourceGroup',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.CreateDefenseResourceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_defense_resource_group(
        self,
        request: waf_openapi_20211001_models.CreateDefenseResourceGroupRequest,
    ) -> waf_openapi_20211001_models.CreateDefenseResourceGroupResponse:
        """
        @summary Creates a protected object group.
        
        @param request: CreateDefenseResourceGroupRequest
        @return: CreateDefenseResourceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_defense_resource_group_with_options(request, runtime)

    async def create_defense_resource_group_async(
        self,
        request: waf_openapi_20211001_models.CreateDefenseResourceGroupRequest,
    ) -> waf_openapi_20211001_models.CreateDefenseResourceGroupResponse:
        """
        @summary Creates a protected object group.
        
        @param request: CreateDefenseResourceGroupRequest
        @return: CreateDefenseResourceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_defense_resource_group_with_options_async(request, runtime)

    def create_defense_rule_with_options(
        self,
        request: waf_openapi_20211001_models.CreateDefenseRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.CreateDefenseRuleResponse:
        """
        @summary Creates a protection rule.
        
        @param request: CreateDefenseRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDefenseRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.defense_scene):
            query['DefenseScene'] = request.defense_scene
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.rules):
            query['Rules'] = request.rules
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDefenseRule',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.CreateDefenseRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_defense_rule_with_options_async(
        self,
        request: waf_openapi_20211001_models.CreateDefenseRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.CreateDefenseRuleResponse:
        """
        @summary Creates a protection rule.
        
        @param request: CreateDefenseRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDefenseRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.defense_scene):
            query['DefenseScene'] = request.defense_scene
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.rules):
            query['Rules'] = request.rules
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDefenseRule',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.CreateDefenseRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_defense_rule(
        self,
        request: waf_openapi_20211001_models.CreateDefenseRuleRequest,
    ) -> waf_openapi_20211001_models.CreateDefenseRuleResponse:
        """
        @summary Creates a protection rule.
        
        @param request: CreateDefenseRuleRequest
        @return: CreateDefenseRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_defense_rule_with_options(request, runtime)

    async def create_defense_rule_async(
        self,
        request: waf_openapi_20211001_models.CreateDefenseRuleRequest,
    ) -> waf_openapi_20211001_models.CreateDefenseRuleResponse:
        """
        @summary Creates a protection rule.
        
        @param request: CreateDefenseRuleRequest
        @return: CreateDefenseRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_defense_rule_with_options_async(request, runtime)

    def create_defense_template_with_options(
        self,
        request: waf_openapi_20211001_models.CreateDefenseTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.CreateDefenseTemplateResponse:
        """
        @summary Creates a protection rule template.
        
        @param request: CreateDefenseTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDefenseTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.defense_scene):
            query['DefenseScene'] = request.defense_scene
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        if not UtilClient.is_unset(request.template_origin):
            query['TemplateOrigin'] = request.template_origin
        if not UtilClient.is_unset(request.template_status):
            query['TemplateStatus'] = request.template_status
        if not UtilClient.is_unset(request.template_type):
            query['TemplateType'] = request.template_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDefenseTemplate',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.CreateDefenseTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_defense_template_with_options_async(
        self,
        request: waf_openapi_20211001_models.CreateDefenseTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.CreateDefenseTemplateResponse:
        """
        @summary Creates a protection rule template.
        
        @param request: CreateDefenseTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDefenseTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.defense_scene):
            query['DefenseScene'] = request.defense_scene
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        if not UtilClient.is_unset(request.template_origin):
            query['TemplateOrigin'] = request.template_origin
        if not UtilClient.is_unset(request.template_status):
            query['TemplateStatus'] = request.template_status
        if not UtilClient.is_unset(request.template_type):
            query['TemplateType'] = request.template_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDefenseTemplate',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.CreateDefenseTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_defense_template(
        self,
        request: waf_openapi_20211001_models.CreateDefenseTemplateRequest,
    ) -> waf_openapi_20211001_models.CreateDefenseTemplateResponse:
        """
        @summary Creates a protection rule template.
        
        @param request: CreateDefenseTemplateRequest
        @return: CreateDefenseTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_defense_template_with_options(request, runtime)

    async def create_defense_template_async(
        self,
        request: waf_openapi_20211001_models.CreateDefenseTemplateRequest,
    ) -> waf_openapi_20211001_models.CreateDefenseTemplateResponse:
        """
        @summary Creates a protection rule template.
        
        @param request: CreateDefenseTemplateRequest
        @return: CreateDefenseTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_defense_template_with_options_async(request, runtime)

    def create_domain_with_options(
        self,
        tmp_req: waf_openapi_20211001_models.CreateDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.CreateDomainResponse:
        """
        @summary Adds a domain name to Web Application Firewall (WAF).
        
        @param tmp_req: CreateDomainRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDomainResponse
        """
        UtilClient.validate_model(tmp_req)
        request = waf_openapi_20211001_models.CreateDomainShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.listen):
            request.listen_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.listen, 'Listen', 'json')
        if not UtilClient.is_unset(tmp_req.redirect):
            request.redirect_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.redirect, 'Redirect', 'json')
        query = {}
        if not UtilClient.is_unset(request.access_type):
            query['AccessType'] = request.access_type
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.listen_shrink):
            query['Listen'] = request.listen_shrink
        if not UtilClient.is_unset(request.redirect_shrink):
            query['Redirect'] = request.redirect_shrink
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDomain',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.CreateDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_domain_with_options_async(
        self,
        tmp_req: waf_openapi_20211001_models.CreateDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.CreateDomainResponse:
        """
        @summary Adds a domain name to Web Application Firewall (WAF).
        
        @param tmp_req: CreateDomainRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDomainResponse
        """
        UtilClient.validate_model(tmp_req)
        request = waf_openapi_20211001_models.CreateDomainShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.listen):
            request.listen_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.listen, 'Listen', 'json')
        if not UtilClient.is_unset(tmp_req.redirect):
            request.redirect_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.redirect, 'Redirect', 'json')
        query = {}
        if not UtilClient.is_unset(request.access_type):
            query['AccessType'] = request.access_type
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.listen_shrink):
            query['Listen'] = request.listen_shrink
        if not UtilClient.is_unset(request.redirect_shrink):
            query['Redirect'] = request.redirect_shrink
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDomain',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.CreateDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_domain(
        self,
        request: waf_openapi_20211001_models.CreateDomainRequest,
    ) -> waf_openapi_20211001_models.CreateDomainResponse:
        """
        @summary Adds a domain name to Web Application Firewall (WAF).
        
        @param request: CreateDomainRequest
        @return: CreateDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_domain_with_options(request, runtime)

    async def create_domain_async(
        self,
        request: waf_openapi_20211001_models.CreateDomainRequest,
    ) -> waf_openapi_20211001_models.CreateDomainResponse:
        """
        @summary Adds a domain name to Web Application Firewall (WAF).
        
        @param request: CreateDomainRequest
        @return: CreateDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_domain_with_options_async(request, runtime)

    def create_major_protection_black_ip_with_options(
        self,
        request: waf_openapi_20211001_models.CreateMajorProtectionBlackIpRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.CreateMajorProtectionBlackIpResponse:
        """
        @summary Creates an IP address blacklist for major event protection.
        
        @description This operation is available only on the China site (aliyun.com).
        
        @param request: CreateMajorProtectionBlackIpRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateMajorProtectionBlackIpResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.expired_time):
            query['ExpiredTime'] = request.expired_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.ip_list):
            query['IpList'] = request.ip_list
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateMajorProtectionBlackIp',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.CreateMajorProtectionBlackIpResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_major_protection_black_ip_with_options_async(
        self,
        request: waf_openapi_20211001_models.CreateMajorProtectionBlackIpRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.CreateMajorProtectionBlackIpResponse:
        """
        @summary Creates an IP address blacklist for major event protection.
        
        @description This operation is available only on the China site (aliyun.com).
        
        @param request: CreateMajorProtectionBlackIpRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateMajorProtectionBlackIpResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.expired_time):
            query['ExpiredTime'] = request.expired_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.ip_list):
            query['IpList'] = request.ip_list
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateMajorProtectionBlackIp',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.CreateMajorProtectionBlackIpResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_major_protection_black_ip(
        self,
        request: waf_openapi_20211001_models.CreateMajorProtectionBlackIpRequest,
    ) -> waf_openapi_20211001_models.CreateMajorProtectionBlackIpResponse:
        """
        @summary Creates an IP address blacklist for major event protection.
        
        @description This operation is available only on the China site (aliyun.com).
        
        @param request: CreateMajorProtectionBlackIpRequest
        @return: CreateMajorProtectionBlackIpResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_major_protection_black_ip_with_options(request, runtime)

    async def create_major_protection_black_ip_async(
        self,
        request: waf_openapi_20211001_models.CreateMajorProtectionBlackIpRequest,
    ) -> waf_openapi_20211001_models.CreateMajorProtectionBlackIpResponse:
        """
        @summary Creates an IP address blacklist for major event protection.
        
        @description This operation is available only on the China site (aliyun.com).
        
        @param request: CreateMajorProtectionBlackIpRequest
        @return: CreateMajorProtectionBlackIpResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_major_protection_black_ip_with_options_async(request, runtime)

    def create_member_accounts_with_options(
        self,
        request: waf_openapi_20211001_models.CreateMemberAccountsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.CreateMemberAccountsResponse:
        """
        @summary Adds members to use the multi-account management feature of Web Application Firewall (WAF).
        
        @param request: CreateMemberAccountsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateMemberAccountsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.member_account_ids):
            query['MemberAccountIds'] = request.member_account_ids
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateMemberAccounts',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.CreateMemberAccountsResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_member_accounts_with_options_async(
        self,
        request: waf_openapi_20211001_models.CreateMemberAccountsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.CreateMemberAccountsResponse:
        """
        @summary Adds members to use the multi-account management feature of Web Application Firewall (WAF).
        
        @param request: CreateMemberAccountsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateMemberAccountsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.member_account_ids):
            query['MemberAccountIds'] = request.member_account_ids
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateMemberAccounts',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.CreateMemberAccountsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_member_accounts(
        self,
        request: waf_openapi_20211001_models.CreateMemberAccountsRequest,
    ) -> waf_openapi_20211001_models.CreateMemberAccountsResponse:
        """
        @summary Adds members to use the multi-account management feature of Web Application Firewall (WAF).
        
        @param request: CreateMemberAccountsRequest
        @return: CreateMemberAccountsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_member_accounts_with_options(request, runtime)

    async def create_member_accounts_async(
        self,
        request: waf_openapi_20211001_models.CreateMemberAccountsRequest,
    ) -> waf_openapi_20211001_models.CreateMemberAccountsResponse:
        """
        @summary Adds members to use the multi-account management feature of Web Application Firewall (WAF).
        
        @param request: CreateMemberAccountsRequest
        @return: CreateMemberAccountsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_member_accounts_with_options_async(request, runtime)

    def create_postpaid_instance_with_options(
        self,
        request: waf_openapi_20211001_models.CreatePostpaidInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.CreatePostpaidInstanceResponse:
        """
        @summary Creates a pay-as-you-go Web Application Firewall (WAF) 3.0 instance.
        
        @param request: CreatePostpaidInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreatePostpaidInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreatePostpaidInstance',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.CreatePostpaidInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_postpaid_instance_with_options_async(
        self,
        request: waf_openapi_20211001_models.CreatePostpaidInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.CreatePostpaidInstanceResponse:
        """
        @summary Creates a pay-as-you-go Web Application Firewall (WAF) 3.0 instance.
        
        @param request: CreatePostpaidInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreatePostpaidInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreatePostpaidInstance',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.CreatePostpaidInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_postpaid_instance(
        self,
        request: waf_openapi_20211001_models.CreatePostpaidInstanceRequest,
    ) -> waf_openapi_20211001_models.CreatePostpaidInstanceResponse:
        """
        @summary Creates a pay-as-you-go Web Application Firewall (WAF) 3.0 instance.
        
        @param request: CreatePostpaidInstanceRequest
        @return: CreatePostpaidInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_postpaid_instance_with_options(request, runtime)

    async def create_postpaid_instance_async(
        self,
        request: waf_openapi_20211001_models.CreatePostpaidInstanceRequest,
    ) -> waf_openapi_20211001_models.CreatePostpaidInstanceResponse:
        """
        @summary Creates a pay-as-you-go Web Application Firewall (WAF) 3.0 instance.
        
        @param request: CreatePostpaidInstanceRequest
        @return: CreatePostpaidInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_postpaid_instance_with_options_async(request, runtime)

    def delete_apisec_abnormal_with_options(
        self,
        request: waf_openapi_20211001_models.DeleteApisecAbnormalRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DeleteApisecAbnormalResponse:
        """
        @summary 删除API安全风险
        
        @param request: DeleteApisecAbnormalRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteApisecAbnormalResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.abnormal_id):
            query['AbnormalId'] = request.abnormal_id
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteApisecAbnormal',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DeleteApisecAbnormalResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_apisec_abnormal_with_options_async(
        self,
        request: waf_openapi_20211001_models.DeleteApisecAbnormalRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DeleteApisecAbnormalResponse:
        """
        @summary 删除API安全风险
        
        @param request: DeleteApisecAbnormalRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteApisecAbnormalResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.abnormal_id):
            query['AbnormalId'] = request.abnormal_id
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteApisecAbnormal',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DeleteApisecAbnormalResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_apisec_abnormal(
        self,
        request: waf_openapi_20211001_models.DeleteApisecAbnormalRequest,
    ) -> waf_openapi_20211001_models.DeleteApisecAbnormalResponse:
        """
        @summary 删除API安全风险
        
        @param request: DeleteApisecAbnormalRequest
        @return: DeleteApisecAbnormalResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_apisec_abnormal_with_options(request, runtime)

    async def delete_apisec_abnormal_async(
        self,
        request: waf_openapi_20211001_models.DeleteApisecAbnormalRequest,
    ) -> waf_openapi_20211001_models.DeleteApisecAbnormalResponse:
        """
        @summary 删除API安全风险
        
        @param request: DeleteApisecAbnormalRequest
        @return: DeleteApisecAbnormalResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_apisec_abnormal_with_options_async(request, runtime)

    def delete_apisec_event_with_options(
        self,
        request: waf_openapi_20211001_models.DeleteApisecEventRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DeleteApisecEventResponse:
        """
        @summary 删除API安全事件
        
        @param request: DeleteApisecEventRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteApisecEventResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.event_id):
            query['EventId'] = request.event_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteApisecEvent',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DeleteApisecEventResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_apisec_event_with_options_async(
        self,
        request: waf_openapi_20211001_models.DeleteApisecEventRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DeleteApisecEventResponse:
        """
        @summary 删除API安全事件
        
        @param request: DeleteApisecEventRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteApisecEventResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.event_id):
            query['EventId'] = request.event_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteApisecEvent',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DeleteApisecEventResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_apisec_event(
        self,
        request: waf_openapi_20211001_models.DeleteApisecEventRequest,
    ) -> waf_openapi_20211001_models.DeleteApisecEventResponse:
        """
        @summary 删除API安全事件
        
        @param request: DeleteApisecEventRequest
        @return: DeleteApisecEventResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_apisec_event_with_options(request, runtime)

    async def delete_apisec_event_async(
        self,
        request: waf_openapi_20211001_models.DeleteApisecEventRequest,
    ) -> waf_openapi_20211001_models.DeleteApisecEventResponse:
        """
        @summary 删除API安全事件
        
        @param request: DeleteApisecEventRequest
        @return: DeleteApisecEventResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_apisec_event_with_options_async(request, runtime)

    def delete_defense_resource_group_with_options(
        self,
        request: waf_openapi_20211001_models.DeleteDefenseResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DeleteDefenseResourceGroupResponse:
        """
        @summary Deletes a protected object group.
        
        @param request: DeleteDefenseResourceGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDefenseResourceGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDefenseResourceGroup',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DeleteDefenseResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_defense_resource_group_with_options_async(
        self,
        request: waf_openapi_20211001_models.DeleteDefenseResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DeleteDefenseResourceGroupResponse:
        """
        @summary Deletes a protected object group.
        
        @param request: DeleteDefenseResourceGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDefenseResourceGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDefenseResourceGroup',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DeleteDefenseResourceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_defense_resource_group(
        self,
        request: waf_openapi_20211001_models.DeleteDefenseResourceGroupRequest,
    ) -> waf_openapi_20211001_models.DeleteDefenseResourceGroupResponse:
        """
        @summary Deletes a protected object group.
        
        @param request: DeleteDefenseResourceGroupRequest
        @return: DeleteDefenseResourceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_defense_resource_group_with_options(request, runtime)

    async def delete_defense_resource_group_async(
        self,
        request: waf_openapi_20211001_models.DeleteDefenseResourceGroupRequest,
    ) -> waf_openapi_20211001_models.DeleteDefenseResourceGroupResponse:
        """
        @summary Deletes a protected object group.
        
        @param request: DeleteDefenseResourceGroupRequest
        @return: DeleteDefenseResourceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_defense_resource_group_with_options_async(request, runtime)

    def delete_defense_rule_with_options(
        self,
        request: waf_openapi_20211001_models.DeleteDefenseRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DeleteDefenseRuleResponse:
        """
        @summary Deletes a protection rule.
        
        @param request: DeleteDefenseRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDefenseRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.rule_ids):
            query['RuleIds'] = request.rule_ids
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDefenseRule',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DeleteDefenseRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_defense_rule_with_options_async(
        self,
        request: waf_openapi_20211001_models.DeleteDefenseRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DeleteDefenseRuleResponse:
        """
        @summary Deletes a protection rule.
        
        @param request: DeleteDefenseRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDefenseRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.rule_ids):
            query['RuleIds'] = request.rule_ids
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDefenseRule',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DeleteDefenseRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_defense_rule(
        self,
        request: waf_openapi_20211001_models.DeleteDefenseRuleRequest,
    ) -> waf_openapi_20211001_models.DeleteDefenseRuleResponse:
        """
        @summary Deletes a protection rule.
        
        @param request: DeleteDefenseRuleRequest
        @return: DeleteDefenseRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_defense_rule_with_options(request, runtime)

    async def delete_defense_rule_async(
        self,
        request: waf_openapi_20211001_models.DeleteDefenseRuleRequest,
    ) -> waf_openapi_20211001_models.DeleteDefenseRuleResponse:
        """
        @summary Deletes a protection rule.
        
        @param request: DeleteDefenseRuleRequest
        @return: DeleteDefenseRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_defense_rule_with_options_async(request, runtime)

    def delete_defense_template_with_options(
        self,
        request: waf_openapi_20211001_models.DeleteDefenseTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DeleteDefenseTemplateResponse:
        """
        @summary Deletes a protection rule template.
        
        @param request: DeleteDefenseTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDefenseTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDefenseTemplate',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DeleteDefenseTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_defense_template_with_options_async(
        self,
        request: waf_openapi_20211001_models.DeleteDefenseTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DeleteDefenseTemplateResponse:
        """
        @summary Deletes a protection rule template.
        
        @param request: DeleteDefenseTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDefenseTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDefenseTemplate',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DeleteDefenseTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_defense_template(
        self,
        request: waf_openapi_20211001_models.DeleteDefenseTemplateRequest,
    ) -> waf_openapi_20211001_models.DeleteDefenseTemplateResponse:
        """
        @summary Deletes a protection rule template.
        
        @param request: DeleteDefenseTemplateRequest
        @return: DeleteDefenseTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_defense_template_with_options(request, runtime)

    async def delete_defense_template_async(
        self,
        request: waf_openapi_20211001_models.DeleteDefenseTemplateRequest,
    ) -> waf_openapi_20211001_models.DeleteDefenseTemplateResponse:
        """
        @summary Deletes a protection rule template.
        
        @param request: DeleteDefenseTemplateRequest
        @return: DeleteDefenseTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_defense_template_with_options_async(request, runtime)

    def delete_domain_with_options(
        self,
        request: waf_openapi_20211001_models.DeleteDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DeleteDomainResponse:
        """
        @summary Deletes a domain name that is added to Web Application Firewall (WAF).
        
        @param request: DeleteDomainRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDomainResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_type):
            query['AccessType'] = request.access_type
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.domain_id):
            query['DomainId'] = request.domain_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDomain',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DeleteDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_domain_with_options_async(
        self,
        request: waf_openapi_20211001_models.DeleteDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DeleteDomainResponse:
        """
        @summary Deletes a domain name that is added to Web Application Firewall (WAF).
        
        @param request: DeleteDomainRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDomainResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_type):
            query['AccessType'] = request.access_type
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.domain_id):
            query['DomainId'] = request.domain_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDomain',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DeleteDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_domain(
        self,
        request: waf_openapi_20211001_models.DeleteDomainRequest,
    ) -> waf_openapi_20211001_models.DeleteDomainResponse:
        """
        @summary Deletes a domain name that is added to Web Application Firewall (WAF).
        
        @param request: DeleteDomainRequest
        @return: DeleteDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_domain_with_options(request, runtime)

    async def delete_domain_async(
        self,
        request: waf_openapi_20211001_models.DeleteDomainRequest,
    ) -> waf_openapi_20211001_models.DeleteDomainResponse:
        """
        @summary Deletes a domain name that is added to Web Application Firewall (WAF).
        
        @param request: DeleteDomainRequest
        @return: DeleteDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_domain_with_options_async(request, runtime)

    def delete_major_protection_black_ip_with_options(
        self,
        request: waf_openapi_20211001_models.DeleteMajorProtectionBlackIpRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DeleteMajorProtectionBlackIpResponse:
        """
        @summary Deletes an IP address blacklist for major event protection.
        
        @param request: DeleteMajorProtectionBlackIpRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteMajorProtectionBlackIpResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.ip_list):
            query['IpList'] = request.ip_list
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteMajorProtectionBlackIp',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DeleteMajorProtectionBlackIpResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_major_protection_black_ip_with_options_async(
        self,
        request: waf_openapi_20211001_models.DeleteMajorProtectionBlackIpRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DeleteMajorProtectionBlackIpResponse:
        """
        @summary Deletes an IP address blacklist for major event protection.
        
        @param request: DeleteMajorProtectionBlackIpRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteMajorProtectionBlackIpResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.ip_list):
            query['IpList'] = request.ip_list
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteMajorProtectionBlackIp',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DeleteMajorProtectionBlackIpResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_major_protection_black_ip(
        self,
        request: waf_openapi_20211001_models.DeleteMajorProtectionBlackIpRequest,
    ) -> waf_openapi_20211001_models.DeleteMajorProtectionBlackIpResponse:
        """
        @summary Deletes an IP address blacklist for major event protection.
        
        @param request: DeleteMajorProtectionBlackIpRequest
        @return: DeleteMajorProtectionBlackIpResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_major_protection_black_ip_with_options(request, runtime)

    async def delete_major_protection_black_ip_async(
        self,
        request: waf_openapi_20211001_models.DeleteMajorProtectionBlackIpRequest,
    ) -> waf_openapi_20211001_models.DeleteMajorProtectionBlackIpResponse:
        """
        @summary Deletes an IP address blacklist for major event protection.
        
        @param request: DeleteMajorProtectionBlackIpRequest
        @return: DeleteMajorProtectionBlackIpResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_major_protection_black_ip_with_options_async(request, runtime)

    def delete_member_account_with_options(
        self,
        request: waf_openapi_20211001_models.DeleteMemberAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DeleteMemberAccountResponse:
        """
        @summary Removes the members that are added for multi-account management in Web Application Firewall (WAF).
        
        @param request: DeleteMemberAccountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteMemberAccountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.member_account_id):
            query['MemberAccountId'] = request.member_account_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteMemberAccount',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DeleteMemberAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_member_account_with_options_async(
        self,
        request: waf_openapi_20211001_models.DeleteMemberAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DeleteMemberAccountResponse:
        """
        @summary Removes the members that are added for multi-account management in Web Application Firewall (WAF).
        
        @param request: DeleteMemberAccountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteMemberAccountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.member_account_id):
            query['MemberAccountId'] = request.member_account_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteMemberAccount',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DeleteMemberAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_member_account(
        self,
        request: waf_openapi_20211001_models.DeleteMemberAccountRequest,
    ) -> waf_openapi_20211001_models.DeleteMemberAccountResponse:
        """
        @summary Removes the members that are added for multi-account management in Web Application Firewall (WAF).
        
        @param request: DeleteMemberAccountRequest
        @return: DeleteMemberAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_member_account_with_options(request, runtime)

    async def delete_member_account_async(
        self,
        request: waf_openapi_20211001_models.DeleteMemberAccountRequest,
    ) -> waf_openapi_20211001_models.DeleteMemberAccountResponse:
        """
        @summary Removes the members that are added for multi-account management in Web Application Firewall (WAF).
        
        @param request: DeleteMemberAccountRequest
        @return: DeleteMemberAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_member_account_with_options_async(request, runtime)

    def describe_account_delegated_status_with_options(
        self,
        request: waf_openapi_20211001_models.DescribeAccountDelegatedStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeAccountDelegatedStatusResponse:
        """
        @summary Queries whether an Alibaba Cloud account is the delegated administrator account of a Web Application Firewall (WAF) instance.
        
        @param request: DescribeAccountDelegatedStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAccountDelegatedStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAccountDelegatedStatus',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeAccountDelegatedStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_account_delegated_status_with_options_async(
        self,
        request: waf_openapi_20211001_models.DescribeAccountDelegatedStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeAccountDelegatedStatusResponse:
        """
        @summary Queries whether an Alibaba Cloud account is the delegated administrator account of a Web Application Firewall (WAF) instance.
        
        @param request: DescribeAccountDelegatedStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAccountDelegatedStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAccountDelegatedStatus',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeAccountDelegatedStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_account_delegated_status(
        self,
        request: waf_openapi_20211001_models.DescribeAccountDelegatedStatusRequest,
    ) -> waf_openapi_20211001_models.DescribeAccountDelegatedStatusResponse:
        """
        @summary Queries whether an Alibaba Cloud account is the delegated administrator account of a Web Application Firewall (WAF) instance.
        
        @param request: DescribeAccountDelegatedStatusRequest
        @return: DescribeAccountDelegatedStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_account_delegated_status_with_options(request, runtime)

    async def describe_account_delegated_status_async(
        self,
        request: waf_openapi_20211001_models.DescribeAccountDelegatedStatusRequest,
    ) -> waf_openapi_20211001_models.DescribeAccountDelegatedStatusResponse:
        """
        @summary Queries whether an Alibaba Cloud account is the delegated administrator account of a Web Application Firewall (WAF) instance.
        
        @param request: DescribeAccountDelegatedStatusRequest
        @return: DescribeAccountDelegatedStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_account_delegated_status_with_options_async(request, runtime)

    def describe_apisec_abnormal_domain_statistic_with_options(
        self,
        request: waf_openapi_20211001_models.DescribeApisecAbnormalDomainStatisticRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeApisecAbnormalDomainStatisticResponse:
        """
        @summary 查询API安全风险站点统计
        
        @param request: DescribeApisecAbnormalDomainStatisticRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeApisecAbnormalDomainStatisticResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.order_way):
            query['OrderWay'] = request.order_way
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApisecAbnormalDomainStatistic',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeApisecAbnormalDomainStatisticResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_apisec_abnormal_domain_statistic_with_options_async(
        self,
        request: waf_openapi_20211001_models.DescribeApisecAbnormalDomainStatisticRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeApisecAbnormalDomainStatisticResponse:
        """
        @summary 查询API安全风险站点统计
        
        @param request: DescribeApisecAbnormalDomainStatisticRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeApisecAbnormalDomainStatisticResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.order_way):
            query['OrderWay'] = request.order_way
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApisecAbnormalDomainStatistic',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeApisecAbnormalDomainStatisticResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_apisec_abnormal_domain_statistic(
        self,
        request: waf_openapi_20211001_models.DescribeApisecAbnormalDomainStatisticRequest,
    ) -> waf_openapi_20211001_models.DescribeApisecAbnormalDomainStatisticResponse:
        """
        @summary 查询API安全风险站点统计
        
        @param request: DescribeApisecAbnormalDomainStatisticRequest
        @return: DescribeApisecAbnormalDomainStatisticResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_apisec_abnormal_domain_statistic_with_options(request, runtime)

    async def describe_apisec_abnormal_domain_statistic_async(
        self,
        request: waf_openapi_20211001_models.DescribeApisecAbnormalDomainStatisticRequest,
    ) -> waf_openapi_20211001_models.DescribeApisecAbnormalDomainStatisticResponse:
        """
        @summary 查询API安全风险站点统计
        
        @param request: DescribeApisecAbnormalDomainStatisticRequest
        @return: DescribeApisecAbnormalDomainStatisticResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_apisec_abnormal_domain_statistic_with_options_async(request, runtime)

    def describe_apisec_asset_trend_with_options(
        self,
        request: waf_openapi_20211001_models.DescribeApisecAssetTrendRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeApisecAssetTrendResponse:
        """
        @summary 查询API安全资产趋势图
        
        @param request: DescribeApisecAssetTrendRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeApisecAssetTrendResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApisecAssetTrend',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeApisecAssetTrendResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_apisec_asset_trend_with_options_async(
        self,
        request: waf_openapi_20211001_models.DescribeApisecAssetTrendRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeApisecAssetTrendResponse:
        """
        @summary 查询API安全资产趋势图
        
        @param request: DescribeApisecAssetTrendRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeApisecAssetTrendResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApisecAssetTrend',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeApisecAssetTrendResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_apisec_asset_trend(
        self,
        request: waf_openapi_20211001_models.DescribeApisecAssetTrendRequest,
    ) -> waf_openapi_20211001_models.DescribeApisecAssetTrendResponse:
        """
        @summary 查询API安全资产趋势图
        
        @param request: DescribeApisecAssetTrendRequest
        @return: DescribeApisecAssetTrendResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_apisec_asset_trend_with_options(request, runtime)

    async def describe_apisec_asset_trend_async(
        self,
        request: waf_openapi_20211001_models.DescribeApisecAssetTrendRequest,
    ) -> waf_openapi_20211001_models.DescribeApisecAssetTrendResponse:
        """
        @summary 查询API安全资产趋势图
        
        @param request: DescribeApisecAssetTrendRequest
        @return: DescribeApisecAssetTrendResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_apisec_asset_trend_with_options_async(request, runtime)

    def describe_apisec_event_domain_statistic_with_options(
        self,
        request: waf_openapi_20211001_models.DescribeApisecEventDomainStatisticRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeApisecEventDomainStatisticResponse:
        """
        @summary 查询API安全事件站点统计
        
        @param request: DescribeApisecEventDomainStatisticRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeApisecEventDomainStatisticResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.order_way):
            query['OrderWay'] = request.order_way
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApisecEventDomainStatistic',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeApisecEventDomainStatisticResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_apisec_event_domain_statistic_with_options_async(
        self,
        request: waf_openapi_20211001_models.DescribeApisecEventDomainStatisticRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeApisecEventDomainStatisticResponse:
        """
        @summary 查询API安全事件站点统计
        
        @param request: DescribeApisecEventDomainStatisticRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeApisecEventDomainStatisticResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.order_way):
            query['OrderWay'] = request.order_way
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApisecEventDomainStatistic',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeApisecEventDomainStatisticResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_apisec_event_domain_statistic(
        self,
        request: waf_openapi_20211001_models.DescribeApisecEventDomainStatisticRequest,
    ) -> waf_openapi_20211001_models.DescribeApisecEventDomainStatisticResponse:
        """
        @summary 查询API安全事件站点统计
        
        @param request: DescribeApisecEventDomainStatisticRequest
        @return: DescribeApisecEventDomainStatisticResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_apisec_event_domain_statistic_with_options(request, runtime)

    async def describe_apisec_event_domain_statistic_async(
        self,
        request: waf_openapi_20211001_models.DescribeApisecEventDomainStatisticRequest,
    ) -> waf_openapi_20211001_models.DescribeApisecEventDomainStatisticResponse:
        """
        @summary 查询API安全事件站点统计
        
        @param request: DescribeApisecEventDomainStatisticRequest
        @return: DescribeApisecEventDomainStatisticResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_apisec_event_domain_statistic_with_options_async(request, runtime)

    def describe_apisec_log_deliveries_with_options(
        self,
        request: waf_openapi_20211001_models.DescribeApisecLogDeliveriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeApisecLogDeliveriesResponse:
        """
        @summary 获取API安全日志订阅列表
        
        @param request: DescribeApisecLogDeliveriesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeApisecLogDeliveriesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApisecLogDeliveries',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeApisecLogDeliveriesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_apisec_log_deliveries_with_options_async(
        self,
        request: waf_openapi_20211001_models.DescribeApisecLogDeliveriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeApisecLogDeliveriesResponse:
        """
        @summary 获取API安全日志订阅列表
        
        @param request: DescribeApisecLogDeliveriesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeApisecLogDeliveriesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApisecLogDeliveries',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeApisecLogDeliveriesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_apisec_log_deliveries(
        self,
        request: waf_openapi_20211001_models.DescribeApisecLogDeliveriesRequest,
    ) -> waf_openapi_20211001_models.DescribeApisecLogDeliveriesResponse:
        """
        @summary 获取API安全日志订阅列表
        
        @param request: DescribeApisecLogDeliveriesRequest
        @return: DescribeApisecLogDeliveriesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_apisec_log_deliveries_with_options(request, runtime)

    async def describe_apisec_log_deliveries_async(
        self,
        request: waf_openapi_20211001_models.DescribeApisecLogDeliveriesRequest,
    ) -> waf_openapi_20211001_models.DescribeApisecLogDeliveriesResponse:
        """
        @summary 获取API安全日志订阅列表
        
        @param request: DescribeApisecLogDeliveriesRequest
        @return: DescribeApisecLogDeliveriesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_apisec_log_deliveries_with_options_async(request, runtime)

    def describe_apisec_sensitive_domain_statistic_with_options(
        self,
        request: waf_openapi_20211001_models.DescribeApisecSensitiveDomainStatisticRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeApisecSensitiveDomainStatisticResponse:
        """
        @summary 查询API安全敏感数据类型统计
        
        @param request: DescribeApisecSensitiveDomainStatisticRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeApisecSensitiveDomainStatisticResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.order_way):
            query['OrderWay'] = request.order_way
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApisecSensitiveDomainStatistic',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeApisecSensitiveDomainStatisticResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_apisec_sensitive_domain_statistic_with_options_async(
        self,
        request: waf_openapi_20211001_models.DescribeApisecSensitiveDomainStatisticRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeApisecSensitiveDomainStatisticResponse:
        """
        @summary 查询API安全敏感数据类型统计
        
        @param request: DescribeApisecSensitiveDomainStatisticRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeApisecSensitiveDomainStatisticResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.order_way):
            query['OrderWay'] = request.order_way
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApisecSensitiveDomainStatistic',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeApisecSensitiveDomainStatisticResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_apisec_sensitive_domain_statistic(
        self,
        request: waf_openapi_20211001_models.DescribeApisecSensitiveDomainStatisticRequest,
    ) -> waf_openapi_20211001_models.DescribeApisecSensitiveDomainStatisticResponse:
        """
        @summary 查询API安全敏感数据类型统计
        
        @param request: DescribeApisecSensitiveDomainStatisticRequest
        @return: DescribeApisecSensitiveDomainStatisticResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_apisec_sensitive_domain_statistic_with_options(request, runtime)

    async def describe_apisec_sensitive_domain_statistic_async(
        self,
        request: waf_openapi_20211001_models.DescribeApisecSensitiveDomainStatisticRequest,
    ) -> waf_openapi_20211001_models.DescribeApisecSensitiveDomainStatisticResponse:
        """
        @summary 查询API安全敏感数据类型统计
        
        @param request: DescribeApisecSensitiveDomainStatisticRequest
        @return: DescribeApisecSensitiveDomainStatisticResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_apisec_sensitive_domain_statistic_with_options_async(request, runtime)

    def describe_apisec_sls_log_stores_with_options(
        self,
        request: waf_openapi_20211001_models.DescribeApisecSlsLogStoresRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeApisecSlsLogStoresResponse:
        """
        @summary 查询日志服务SLS的LogStore列表
        
        @param request: DescribeApisecSlsLogStoresRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeApisecSlsLogStoresResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.log_region_id):
            query['LogRegionId'] = request.log_region_id
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApisecSlsLogStores',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeApisecSlsLogStoresResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_apisec_sls_log_stores_with_options_async(
        self,
        request: waf_openapi_20211001_models.DescribeApisecSlsLogStoresRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeApisecSlsLogStoresResponse:
        """
        @summary 查询日志服务SLS的LogStore列表
        
        @param request: DescribeApisecSlsLogStoresRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeApisecSlsLogStoresResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.log_region_id):
            query['LogRegionId'] = request.log_region_id
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApisecSlsLogStores',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeApisecSlsLogStoresResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_apisec_sls_log_stores(
        self,
        request: waf_openapi_20211001_models.DescribeApisecSlsLogStoresRequest,
    ) -> waf_openapi_20211001_models.DescribeApisecSlsLogStoresResponse:
        """
        @summary 查询日志服务SLS的LogStore列表
        
        @param request: DescribeApisecSlsLogStoresRequest
        @return: DescribeApisecSlsLogStoresResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_apisec_sls_log_stores_with_options(request, runtime)

    async def describe_apisec_sls_log_stores_async(
        self,
        request: waf_openapi_20211001_models.DescribeApisecSlsLogStoresRequest,
    ) -> waf_openapi_20211001_models.DescribeApisecSlsLogStoresResponse:
        """
        @summary 查询日志服务SLS的LogStore列表
        
        @param request: DescribeApisecSlsLogStoresRequest
        @return: DescribeApisecSlsLogStoresResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_apisec_sls_log_stores_with_options_async(request, runtime)

    def describe_apisec_sls_projects_with_options(
        self,
        request: waf_openapi_20211001_models.DescribeApisecSlsProjectsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeApisecSlsProjectsResponse:
        """
        @summary 查询日志服务SLS的Project列表
        
        @param request: DescribeApisecSlsProjectsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeApisecSlsProjectsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.log_region_id):
            query['LogRegionId'] = request.log_region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApisecSlsProjects',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeApisecSlsProjectsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_apisec_sls_projects_with_options_async(
        self,
        request: waf_openapi_20211001_models.DescribeApisecSlsProjectsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeApisecSlsProjectsResponse:
        """
        @summary 查询日志服务SLS的Project列表
        
        @param request: DescribeApisecSlsProjectsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeApisecSlsProjectsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.log_region_id):
            query['LogRegionId'] = request.log_region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApisecSlsProjects',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeApisecSlsProjectsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_apisec_sls_projects(
        self,
        request: waf_openapi_20211001_models.DescribeApisecSlsProjectsRequest,
    ) -> waf_openapi_20211001_models.DescribeApisecSlsProjectsResponse:
        """
        @summary 查询日志服务SLS的Project列表
        
        @param request: DescribeApisecSlsProjectsRequest
        @return: DescribeApisecSlsProjectsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_apisec_sls_projects_with_options(request, runtime)

    async def describe_apisec_sls_projects_async(
        self,
        request: waf_openapi_20211001_models.DescribeApisecSlsProjectsRequest,
    ) -> waf_openapi_20211001_models.DescribeApisecSlsProjectsResponse:
        """
        @summary 查询日志服务SLS的Project列表
        
        @param request: DescribeApisecSlsProjectsRequest
        @return: DescribeApisecSlsProjectsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_apisec_sls_projects_with_options_async(request, runtime)

    def describe_cert_detail_with_options(
        self,
        request: waf_openapi_20211001_models.DescribeCertDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeCertDetailResponse:
        """
        @summary Queries the details of a certificate, such as the certificate name, expiration time, issuance time, and associated domain name.
        
        @param request: DescribeCertDetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCertDetailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cert_identifier):
            query['CertIdentifier'] = request.cert_identifier
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCertDetail',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeCertDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cert_detail_with_options_async(
        self,
        request: waf_openapi_20211001_models.DescribeCertDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeCertDetailResponse:
        """
        @summary Queries the details of a certificate, such as the certificate name, expiration time, issuance time, and associated domain name.
        
        @param request: DescribeCertDetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCertDetailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cert_identifier):
            query['CertIdentifier'] = request.cert_identifier
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCertDetail',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeCertDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cert_detail(
        self,
        request: waf_openapi_20211001_models.DescribeCertDetailRequest,
    ) -> waf_openapi_20211001_models.DescribeCertDetailResponse:
        """
        @summary Queries the details of a certificate, such as the certificate name, expiration time, issuance time, and associated domain name.
        
        @param request: DescribeCertDetailRequest
        @return: DescribeCertDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_cert_detail_with_options(request, runtime)

    async def describe_cert_detail_async(
        self,
        request: waf_openapi_20211001_models.DescribeCertDetailRequest,
    ) -> waf_openapi_20211001_models.DescribeCertDetailResponse:
        """
        @summary Queries the details of a certificate, such as the certificate name, expiration time, issuance time, and associated domain name.
        
        @param request: DescribeCertDetailRequest
        @return: DescribeCertDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_cert_detail_with_options_async(request, runtime)

    def describe_certs_with_options(
        self,
        request: waf_openapi_20211001_models.DescribeCertsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeCertsResponse:
        """
        @summary Queries the certificates issued for your domain names that are added to Web Application Firewall (WAF).
        
        @param request: DescribeCertsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCertsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.algorithm):
            query['Algorithm'] = request.algorithm
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCerts',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeCertsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_certs_with_options_async(
        self,
        request: waf_openapi_20211001_models.DescribeCertsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeCertsResponse:
        """
        @summary Queries the certificates issued for your domain names that are added to Web Application Firewall (WAF).
        
        @param request: DescribeCertsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCertsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.algorithm):
            query['Algorithm'] = request.algorithm
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCerts',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeCertsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_certs(
        self,
        request: waf_openapi_20211001_models.DescribeCertsRequest,
    ) -> waf_openapi_20211001_models.DescribeCertsResponse:
        """
        @summary Queries the certificates issued for your domain names that are added to Web Application Firewall (WAF).
        
        @param request: DescribeCertsRequest
        @return: DescribeCertsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_certs_with_options(request, runtime)

    async def describe_certs_async(
        self,
        request: waf_openapi_20211001_models.DescribeCertsRequest,
    ) -> waf_openapi_20211001_models.DescribeCertsResponse:
        """
        @summary Queries the certificates issued for your domain names that are added to Web Application Firewall (WAF).
        
        @param request: DescribeCertsRequest
        @return: DescribeCertsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_certs_with_options_async(request, runtime)

    def describe_cloud_resources_with_options(
        self,
        request: waf_openapi_20211001_models.DescribeCloudResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeCloudResourcesResponse:
        """
        @summary Queries cloud service resources that are added to Web Application Firewall (WAF).
        
        @param request: DescribeCloudResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCloudResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_user_id):
            query['OwnerUserId'] = request.owner_user_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_domain):
            query['ResourceDomain'] = request.resource_domain
        if not UtilClient.is_unset(request.resource_function):
            query['ResourceFunction'] = request.resource_function
        if not UtilClient.is_unset(request.resource_instance_id):
            query['ResourceInstanceId'] = request.resource_instance_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.resource_name):
            query['ResourceName'] = request.resource_name
        if not UtilClient.is_unset(request.resource_product):
            query['ResourceProduct'] = request.resource_product
        if not UtilClient.is_unset(request.resource_region_id):
            query['ResourceRegionId'] = request.resource_region_id
        if not UtilClient.is_unset(request.resource_route_name):
            query['ResourceRouteName'] = request.resource_route_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCloudResources',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeCloudResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cloud_resources_with_options_async(
        self,
        request: waf_openapi_20211001_models.DescribeCloudResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeCloudResourcesResponse:
        """
        @summary Queries cloud service resources that are added to Web Application Firewall (WAF).
        
        @param request: DescribeCloudResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCloudResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_user_id):
            query['OwnerUserId'] = request.owner_user_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_domain):
            query['ResourceDomain'] = request.resource_domain
        if not UtilClient.is_unset(request.resource_function):
            query['ResourceFunction'] = request.resource_function
        if not UtilClient.is_unset(request.resource_instance_id):
            query['ResourceInstanceId'] = request.resource_instance_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.resource_name):
            query['ResourceName'] = request.resource_name
        if not UtilClient.is_unset(request.resource_product):
            query['ResourceProduct'] = request.resource_product
        if not UtilClient.is_unset(request.resource_region_id):
            query['ResourceRegionId'] = request.resource_region_id
        if not UtilClient.is_unset(request.resource_route_name):
            query['ResourceRouteName'] = request.resource_route_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCloudResources',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeCloudResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cloud_resources(
        self,
        request: waf_openapi_20211001_models.DescribeCloudResourcesRequest,
    ) -> waf_openapi_20211001_models.DescribeCloudResourcesResponse:
        """
        @summary Queries cloud service resources that are added to Web Application Firewall (WAF).
        
        @param request: DescribeCloudResourcesRequest
        @return: DescribeCloudResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_cloud_resources_with_options(request, runtime)

    async def describe_cloud_resources_async(
        self,
        request: waf_openapi_20211001_models.DescribeCloudResourcesRequest,
    ) -> waf_openapi_20211001_models.DescribeCloudResourcesResponse:
        """
        @summary Queries cloud service resources that are added to Web Application Firewall (WAF).
        
        @param request: DescribeCloudResourcesRequest
        @return: DescribeCloudResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_cloud_resources_with_options_async(request, runtime)

    def describe_defense_resource_with_options(
        self,
        request: waf_openapi_20211001_models.DescribeDefenseResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeDefenseResourceResponse:
        """
        @summary Queries the information about a protected object.
        
        @param request: DescribeDefenseResourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDefenseResourceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource):
            query['Resource'] = request.resource
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDefenseResource',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeDefenseResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_defense_resource_with_options_async(
        self,
        request: waf_openapi_20211001_models.DescribeDefenseResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeDefenseResourceResponse:
        """
        @summary Queries the information about a protected object.
        
        @param request: DescribeDefenseResourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDefenseResourceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource):
            query['Resource'] = request.resource
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDefenseResource',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeDefenseResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_defense_resource(
        self,
        request: waf_openapi_20211001_models.DescribeDefenseResourceRequest,
    ) -> waf_openapi_20211001_models.DescribeDefenseResourceResponse:
        """
        @summary Queries the information about a protected object.
        
        @param request: DescribeDefenseResourceRequest
        @return: DescribeDefenseResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_defense_resource_with_options(request, runtime)

    async def describe_defense_resource_async(
        self,
        request: waf_openapi_20211001_models.DescribeDefenseResourceRequest,
    ) -> waf_openapi_20211001_models.DescribeDefenseResourceResponse:
        """
        @summary Queries the information about a protected object.
        
        @param request: DescribeDefenseResourceRequest
        @return: DescribeDefenseResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_defense_resource_with_options_async(request, runtime)

    def describe_defense_resource_group_with_options(
        self,
        request: waf_openapi_20211001_models.DescribeDefenseResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeDefenseResourceGroupResponse:
        """
        @summary Queries the information about a protected object group.
        
        @param request: DescribeDefenseResourceGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDefenseResourceGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDefenseResourceGroup',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeDefenseResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_defense_resource_group_with_options_async(
        self,
        request: waf_openapi_20211001_models.DescribeDefenseResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeDefenseResourceGroupResponse:
        """
        @summary Queries the information about a protected object group.
        
        @param request: DescribeDefenseResourceGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDefenseResourceGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDefenseResourceGroup',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeDefenseResourceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_defense_resource_group(
        self,
        request: waf_openapi_20211001_models.DescribeDefenseResourceGroupRequest,
    ) -> waf_openapi_20211001_models.DescribeDefenseResourceGroupResponse:
        """
        @summary Queries the information about a protected object group.
        
        @param request: DescribeDefenseResourceGroupRequest
        @return: DescribeDefenseResourceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_defense_resource_group_with_options(request, runtime)

    async def describe_defense_resource_group_async(
        self,
        request: waf_openapi_20211001_models.DescribeDefenseResourceGroupRequest,
    ) -> waf_openapi_20211001_models.DescribeDefenseResourceGroupResponse:
        """
        @summary Queries the information about a protected object group.
        
        @param request: DescribeDefenseResourceGroupRequest
        @return: DescribeDefenseResourceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_defense_resource_group_with_options_async(request, runtime)

    def describe_defense_resource_group_names_with_options(
        self,
        request: waf_openapi_20211001_models.DescribeDefenseResourceGroupNamesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeDefenseResourceGroupNamesResponse:
        """
        @summary Queries the names of protected object groups.
        
        @param request: DescribeDefenseResourceGroupNamesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDefenseResourceGroupNamesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_name_like):
            query['GroupNameLike'] = request.group_name_like
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDefenseResourceGroupNames',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeDefenseResourceGroupNamesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_defense_resource_group_names_with_options_async(
        self,
        request: waf_openapi_20211001_models.DescribeDefenseResourceGroupNamesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeDefenseResourceGroupNamesResponse:
        """
        @summary Queries the names of protected object groups.
        
        @param request: DescribeDefenseResourceGroupNamesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDefenseResourceGroupNamesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_name_like):
            query['GroupNameLike'] = request.group_name_like
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDefenseResourceGroupNames',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeDefenseResourceGroupNamesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_defense_resource_group_names(
        self,
        request: waf_openapi_20211001_models.DescribeDefenseResourceGroupNamesRequest,
    ) -> waf_openapi_20211001_models.DescribeDefenseResourceGroupNamesResponse:
        """
        @summary Queries the names of protected object groups.
        
        @param request: DescribeDefenseResourceGroupNamesRequest
        @return: DescribeDefenseResourceGroupNamesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_defense_resource_group_names_with_options(request, runtime)

    async def describe_defense_resource_group_names_async(
        self,
        request: waf_openapi_20211001_models.DescribeDefenseResourceGroupNamesRequest,
    ) -> waf_openapi_20211001_models.DescribeDefenseResourceGroupNamesResponse:
        """
        @summary Queries the names of protected object groups.
        
        @param request: DescribeDefenseResourceGroupNamesRequest
        @return: DescribeDefenseResourceGroupNamesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_defense_resource_group_names_with_options_async(request, runtime)

    def describe_defense_resource_groups_with_options(
        self,
        request: waf_openapi_20211001_models.DescribeDefenseResourceGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeDefenseResourceGroupsResponse:
        """
        @summary Performs a pagination query to retrieve the information about protected object groups.
        
        @param request: DescribeDefenseResourceGroupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDefenseResourceGroupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_name_like):
            query['GroupNameLike'] = request.group_name_like
        if not UtilClient.is_unset(request.group_names):
            query['GroupNames'] = request.group_names
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDefenseResourceGroups',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeDefenseResourceGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_defense_resource_groups_with_options_async(
        self,
        request: waf_openapi_20211001_models.DescribeDefenseResourceGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeDefenseResourceGroupsResponse:
        """
        @summary Performs a pagination query to retrieve the information about protected object groups.
        
        @param request: DescribeDefenseResourceGroupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDefenseResourceGroupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_name_like):
            query['GroupNameLike'] = request.group_name_like
        if not UtilClient.is_unset(request.group_names):
            query['GroupNames'] = request.group_names
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDefenseResourceGroups',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeDefenseResourceGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_defense_resource_groups(
        self,
        request: waf_openapi_20211001_models.DescribeDefenseResourceGroupsRequest,
    ) -> waf_openapi_20211001_models.DescribeDefenseResourceGroupsResponse:
        """
        @summary Performs a pagination query to retrieve the information about protected object groups.
        
        @param request: DescribeDefenseResourceGroupsRequest
        @return: DescribeDefenseResourceGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_defense_resource_groups_with_options(request, runtime)

    async def describe_defense_resource_groups_async(
        self,
        request: waf_openapi_20211001_models.DescribeDefenseResourceGroupsRequest,
    ) -> waf_openapi_20211001_models.DescribeDefenseResourceGroupsResponse:
        """
        @summary Performs a pagination query to retrieve the information about protected object groups.
        
        @param request: DescribeDefenseResourceGroupsRequest
        @return: DescribeDefenseResourceGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_defense_resource_groups_with_options_async(request, runtime)

    def describe_defense_resource_names_with_options(
        self,
        request: waf_openapi_20211001_models.DescribeDefenseResourceNamesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeDefenseResourceNamesResponse:
        """
        @summary Performs a pagination query to retrieve the names of protected objects.
        
        @param request: DescribeDefenseResourceNamesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDefenseResourceNamesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource):
            query['Resource'] = request.resource
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDefenseResourceNames',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeDefenseResourceNamesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_defense_resource_names_with_options_async(
        self,
        request: waf_openapi_20211001_models.DescribeDefenseResourceNamesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeDefenseResourceNamesResponse:
        """
        @summary Performs a pagination query to retrieve the names of protected objects.
        
        @param request: DescribeDefenseResourceNamesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDefenseResourceNamesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource):
            query['Resource'] = request.resource
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDefenseResourceNames',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeDefenseResourceNamesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_defense_resource_names(
        self,
        request: waf_openapi_20211001_models.DescribeDefenseResourceNamesRequest,
    ) -> waf_openapi_20211001_models.DescribeDefenseResourceNamesResponse:
        """
        @summary Performs a pagination query to retrieve the names of protected objects.
        
        @param request: DescribeDefenseResourceNamesRequest
        @return: DescribeDefenseResourceNamesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_defense_resource_names_with_options(request, runtime)

    async def describe_defense_resource_names_async(
        self,
        request: waf_openapi_20211001_models.DescribeDefenseResourceNamesRequest,
    ) -> waf_openapi_20211001_models.DescribeDefenseResourceNamesResponse:
        """
        @summary Performs a pagination query to retrieve the names of protected objects.
        
        @param request: DescribeDefenseResourceNamesRequest
        @return: DescribeDefenseResourceNamesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_defense_resource_names_with_options_async(request, runtime)

    def describe_defense_resource_templates_with_options(
        self,
        request: waf_openapi_20211001_models.DescribeDefenseResourceTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeDefenseResourceTemplatesResponse:
        """
        @summary Queries the protection templates that are associated with a protected object or protected object group.
        
        @param request: DescribeDefenseResourceTemplatesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDefenseResourceTemplatesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource):
            query['Resource'] = request.resource
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        if not UtilClient.is_unset(request.rule_type):
            query['RuleType'] = request.rule_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDefenseResourceTemplates',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeDefenseResourceTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_defense_resource_templates_with_options_async(
        self,
        request: waf_openapi_20211001_models.DescribeDefenseResourceTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeDefenseResourceTemplatesResponse:
        """
        @summary Queries the protection templates that are associated with a protected object or protected object group.
        
        @param request: DescribeDefenseResourceTemplatesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDefenseResourceTemplatesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource):
            query['Resource'] = request.resource
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        if not UtilClient.is_unset(request.rule_type):
            query['RuleType'] = request.rule_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDefenseResourceTemplates',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeDefenseResourceTemplatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_defense_resource_templates(
        self,
        request: waf_openapi_20211001_models.DescribeDefenseResourceTemplatesRequest,
    ) -> waf_openapi_20211001_models.DescribeDefenseResourceTemplatesResponse:
        """
        @summary Queries the protection templates that are associated with a protected object or protected object group.
        
        @param request: DescribeDefenseResourceTemplatesRequest
        @return: DescribeDefenseResourceTemplatesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_defense_resource_templates_with_options(request, runtime)

    async def describe_defense_resource_templates_async(
        self,
        request: waf_openapi_20211001_models.DescribeDefenseResourceTemplatesRequest,
    ) -> waf_openapi_20211001_models.DescribeDefenseResourceTemplatesResponse:
        """
        @summary Queries the protection templates that are associated with a protected object or protected object group.
        
        @param request: DescribeDefenseResourceTemplatesRequest
        @return: DescribeDefenseResourceTemplatesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_defense_resource_templates_with_options_async(request, runtime)

    def describe_defense_resources_with_options(
        self,
        request: waf_openapi_20211001_models.DescribeDefenseResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeDefenseResourcesResponse:
        """
        @summary Queries protected objects by page.
        
        @param request: DescribeDefenseResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDefenseResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query):
            query['Query'] = request.query
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDefenseResources',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeDefenseResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_defense_resources_with_options_async(
        self,
        request: waf_openapi_20211001_models.DescribeDefenseResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeDefenseResourcesResponse:
        """
        @summary Queries protected objects by page.
        
        @param request: DescribeDefenseResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDefenseResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query):
            query['Query'] = request.query
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDefenseResources',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeDefenseResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_defense_resources(
        self,
        request: waf_openapi_20211001_models.DescribeDefenseResourcesRequest,
    ) -> waf_openapi_20211001_models.DescribeDefenseResourcesResponse:
        """
        @summary Queries protected objects by page.
        
        @param request: DescribeDefenseResourcesRequest
        @return: DescribeDefenseResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_defense_resources_with_options(request, runtime)

    async def describe_defense_resources_async(
        self,
        request: waf_openapi_20211001_models.DescribeDefenseResourcesRequest,
    ) -> waf_openapi_20211001_models.DescribeDefenseResourcesResponse:
        """
        @summary Queries protected objects by page.
        
        @param request: DescribeDefenseResourcesRequest
        @return: DescribeDefenseResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_defense_resources_with_options_async(request, runtime)

    def describe_defense_rule_with_options(
        self,
        request: waf_openapi_20211001_models.DescribeDefenseRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeDefenseRuleResponse:
        """
        @summary Queries a protection rule.
        
        @param request: DescribeDefenseRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDefenseRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDefenseRule',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeDefenseRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_defense_rule_with_options_async(
        self,
        request: waf_openapi_20211001_models.DescribeDefenseRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeDefenseRuleResponse:
        """
        @summary Queries a protection rule.
        
        @param request: DescribeDefenseRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDefenseRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDefenseRule',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeDefenseRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_defense_rule(
        self,
        request: waf_openapi_20211001_models.DescribeDefenseRuleRequest,
    ) -> waf_openapi_20211001_models.DescribeDefenseRuleResponse:
        """
        @summary Queries a protection rule.
        
        @param request: DescribeDefenseRuleRequest
        @return: DescribeDefenseRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_defense_rule_with_options(request, runtime)

    async def describe_defense_rule_async(
        self,
        request: waf_openapi_20211001_models.DescribeDefenseRuleRequest,
    ) -> waf_openapi_20211001_models.DescribeDefenseRuleResponse:
        """
        @summary Queries a protection rule.
        
        @param request: DescribeDefenseRuleRequest
        @return: DescribeDefenseRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_defense_rule_with_options_async(request, runtime)

    def describe_defense_rules_with_options(
        self,
        request: waf_openapi_20211001_models.DescribeDefenseRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeDefenseRulesResponse:
        """
        @summary Queries protection rules by page.
        
        @param request: DescribeDefenseRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDefenseRulesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query):
            query['Query'] = request.query
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.rule_type):
            query['RuleType'] = request.rule_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDefenseRules',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeDefenseRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_defense_rules_with_options_async(
        self,
        request: waf_openapi_20211001_models.DescribeDefenseRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeDefenseRulesResponse:
        """
        @summary Queries protection rules by page.
        
        @param request: DescribeDefenseRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDefenseRulesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query):
            query['Query'] = request.query
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.rule_type):
            query['RuleType'] = request.rule_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDefenseRules',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeDefenseRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_defense_rules(
        self,
        request: waf_openapi_20211001_models.DescribeDefenseRulesRequest,
    ) -> waf_openapi_20211001_models.DescribeDefenseRulesResponse:
        """
        @summary Queries protection rules by page.
        
        @param request: DescribeDefenseRulesRequest
        @return: DescribeDefenseRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_defense_rules_with_options(request, runtime)

    async def describe_defense_rules_async(
        self,
        request: waf_openapi_20211001_models.DescribeDefenseRulesRequest,
    ) -> waf_openapi_20211001_models.DescribeDefenseRulesResponse:
        """
        @summary Queries protection rules by page.
        
        @param request: DescribeDefenseRulesRequest
        @return: DescribeDefenseRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_defense_rules_with_options_async(request, runtime)

    def describe_defense_template_with_options(
        self,
        request: waf_openapi_20211001_models.DescribeDefenseTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeDefenseTemplateResponse:
        """
        @summary Queries a protection rule template.
        
        @param request: DescribeDefenseTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDefenseTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDefenseTemplate',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeDefenseTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_defense_template_with_options_async(
        self,
        request: waf_openapi_20211001_models.DescribeDefenseTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeDefenseTemplateResponse:
        """
        @summary Queries a protection rule template.
        
        @param request: DescribeDefenseTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDefenseTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDefenseTemplate',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeDefenseTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_defense_template(
        self,
        request: waf_openapi_20211001_models.DescribeDefenseTemplateRequest,
    ) -> waf_openapi_20211001_models.DescribeDefenseTemplateResponse:
        """
        @summary Queries a protection rule template.
        
        @param request: DescribeDefenseTemplateRequest
        @return: DescribeDefenseTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_defense_template_with_options(request, runtime)

    async def describe_defense_template_async(
        self,
        request: waf_openapi_20211001_models.DescribeDefenseTemplateRequest,
    ) -> waf_openapi_20211001_models.DescribeDefenseTemplateResponse:
        """
        @summary Queries a protection rule template.
        
        @param request: DescribeDefenseTemplateRequest
        @return: DescribeDefenseTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_defense_template_with_options_async(request, runtime)

    def describe_defense_template_valid_groups_with_options(
        self,
        request: waf_openapi_20211001_models.DescribeDefenseTemplateValidGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeDefenseTemplateValidGroupsResponse:
        """
        @summary Queries the names of protected object groups for which a protection template can take effect.
        
        @param request: DescribeDefenseTemplateValidGroupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDefenseTemplateValidGroupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.defense_scene):
            query['DefenseScene'] = request.defense_scene
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDefenseTemplateValidGroups',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeDefenseTemplateValidGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_defense_template_valid_groups_with_options_async(
        self,
        request: waf_openapi_20211001_models.DescribeDefenseTemplateValidGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeDefenseTemplateValidGroupsResponse:
        """
        @summary Queries the names of protected object groups for which a protection template can take effect.
        
        @param request: DescribeDefenseTemplateValidGroupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDefenseTemplateValidGroupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.defense_scene):
            query['DefenseScene'] = request.defense_scene
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDefenseTemplateValidGroups',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeDefenseTemplateValidGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_defense_template_valid_groups(
        self,
        request: waf_openapi_20211001_models.DescribeDefenseTemplateValidGroupsRequest,
    ) -> waf_openapi_20211001_models.DescribeDefenseTemplateValidGroupsResponse:
        """
        @summary Queries the names of protected object groups for which a protection template can take effect.
        
        @param request: DescribeDefenseTemplateValidGroupsRequest
        @return: DescribeDefenseTemplateValidGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_defense_template_valid_groups_with_options(request, runtime)

    async def describe_defense_template_valid_groups_async(
        self,
        request: waf_openapi_20211001_models.DescribeDefenseTemplateValidGroupsRequest,
    ) -> waf_openapi_20211001_models.DescribeDefenseTemplateValidGroupsResponse:
        """
        @summary Queries the names of protected object groups for which a protection template can take effect.
        
        @param request: DescribeDefenseTemplateValidGroupsRequest
        @return: DescribeDefenseTemplateValidGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_defense_template_valid_groups_with_options_async(request, runtime)

    def describe_defense_templates_with_options(
        self,
        request: waf_openapi_20211001_models.DescribeDefenseTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeDefenseTemplatesResponse:
        """
        @summary Performs a paging query to retrieve protection templates.
        
        @param request: DescribeDefenseTemplatesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDefenseTemplatesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.defense_scene):
            query['DefenseScene'] = request.defense_scene
        if not UtilClient.is_unset(request.defense_sub_scene):
            query['DefenseSubScene'] = request.defense_sub_scene
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource):
            query['Resource'] = request.resource
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.template_type):
            query['TemplateType'] = request.template_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDefenseTemplates',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeDefenseTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_defense_templates_with_options_async(
        self,
        request: waf_openapi_20211001_models.DescribeDefenseTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeDefenseTemplatesResponse:
        """
        @summary Performs a paging query to retrieve protection templates.
        
        @param request: DescribeDefenseTemplatesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDefenseTemplatesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.defense_scene):
            query['DefenseScene'] = request.defense_scene
        if not UtilClient.is_unset(request.defense_sub_scene):
            query['DefenseSubScene'] = request.defense_sub_scene
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource):
            query['Resource'] = request.resource
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.template_type):
            query['TemplateType'] = request.template_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDefenseTemplates',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeDefenseTemplatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_defense_templates(
        self,
        request: waf_openapi_20211001_models.DescribeDefenseTemplatesRequest,
    ) -> waf_openapi_20211001_models.DescribeDefenseTemplatesResponse:
        """
        @summary Performs a paging query to retrieve protection templates.
        
        @param request: DescribeDefenseTemplatesRequest
        @return: DescribeDefenseTemplatesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_defense_templates_with_options(request, runtime)

    async def describe_defense_templates_async(
        self,
        request: waf_openapi_20211001_models.DescribeDefenseTemplatesRequest,
    ) -> waf_openapi_20211001_models.DescribeDefenseTemplatesResponse:
        """
        @summary Performs a paging query to retrieve protection templates.
        
        @param request: DescribeDefenseTemplatesRequest
        @return: DescribeDefenseTemplatesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_defense_templates_with_options_async(request, runtime)

    def describe_domain_dnsrecord_with_options(
        self,
        request: waf_openapi_20211001_models.DescribeDomainDNSRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeDomainDNSRecordResponse:
        """
        @summary Checks whether the Domain Name System (DNS) settings of a domain name are properly configured.
        
        @param request: DescribeDomainDNSRecordRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainDNSRecordResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainDNSRecord',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeDomainDNSRecordResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_dnsrecord_with_options_async(
        self,
        request: waf_openapi_20211001_models.DescribeDomainDNSRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeDomainDNSRecordResponse:
        """
        @summary Checks whether the Domain Name System (DNS) settings of a domain name are properly configured.
        
        @param request: DescribeDomainDNSRecordRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainDNSRecordResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainDNSRecord',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeDomainDNSRecordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_dnsrecord(
        self,
        request: waf_openapi_20211001_models.DescribeDomainDNSRecordRequest,
    ) -> waf_openapi_20211001_models.DescribeDomainDNSRecordResponse:
        """
        @summary Checks whether the Domain Name System (DNS) settings of a domain name are properly configured.
        
        @param request: DescribeDomainDNSRecordRequest
        @return: DescribeDomainDNSRecordResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_dnsrecord_with_options(request, runtime)

    async def describe_domain_dnsrecord_async(
        self,
        request: waf_openapi_20211001_models.DescribeDomainDNSRecordRequest,
    ) -> waf_openapi_20211001_models.DescribeDomainDNSRecordResponse:
        """
        @summary Checks whether the Domain Name System (DNS) settings of a domain name are properly configured.
        
        @param request: DescribeDomainDNSRecordRequest
        @return: DescribeDomainDNSRecordResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_dnsrecord_with_options_async(request, runtime)

    def describe_domain_detail_with_options(
        self,
        request: waf_openapi_20211001_models.DescribeDomainDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeDomainDetailResponse:
        """
        @summary Queries the details of a domain name that is added to Web Application Firewall (WAF).
        
        @param request: DescribeDomainDetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainDetailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainDetail',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeDomainDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_detail_with_options_async(
        self,
        request: waf_openapi_20211001_models.DescribeDomainDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeDomainDetailResponse:
        """
        @summary Queries the details of a domain name that is added to Web Application Firewall (WAF).
        
        @param request: DescribeDomainDetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainDetailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainDetail',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeDomainDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_detail(
        self,
        request: waf_openapi_20211001_models.DescribeDomainDetailRequest,
    ) -> waf_openapi_20211001_models.DescribeDomainDetailResponse:
        """
        @summary Queries the details of a domain name that is added to Web Application Firewall (WAF).
        
        @param request: DescribeDomainDetailRequest
        @return: DescribeDomainDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_detail_with_options(request, runtime)

    async def describe_domain_detail_async(
        self,
        request: waf_openapi_20211001_models.DescribeDomainDetailRequest,
    ) -> waf_openapi_20211001_models.DescribeDomainDetailResponse:
        """
        @summary Queries the details of a domain name that is added to Web Application Firewall (WAF).
        
        @param request: DescribeDomainDetailRequest
        @return: DescribeDomainDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_detail_with_options_async(request, runtime)

    def describe_domains_with_options(
        self,
        request: waf_openapi_20211001_models.DescribeDomainsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeDomainsResponse:
        """
        @summary Queries the domain names that are added to Web Application Firewall (WAF).
        
        @param request: DescribeDomainsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backend):
            query['Backend'] = request.backend
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomains',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeDomainsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domains_with_options_async(
        self,
        request: waf_openapi_20211001_models.DescribeDomainsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeDomainsResponse:
        """
        @summary Queries the domain names that are added to Web Application Firewall (WAF).
        
        @param request: DescribeDomainsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backend):
            query['Backend'] = request.backend
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomains',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeDomainsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domains(
        self,
        request: waf_openapi_20211001_models.DescribeDomainsRequest,
    ) -> waf_openapi_20211001_models.DescribeDomainsResponse:
        """
        @summary Queries the domain names that are added to Web Application Firewall (WAF).
        
        @param request: DescribeDomainsRequest
        @return: DescribeDomainsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_domains_with_options(request, runtime)

    async def describe_domains_async(
        self,
        request: waf_openapi_20211001_models.DescribeDomainsRequest,
    ) -> waf_openapi_20211001_models.DescribeDomainsResponse:
        """
        @summary Queries the domain names that are added to Web Application Firewall (WAF).
        
        @param request: DescribeDomainsRequest
        @return: DescribeDomainsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_domains_with_options_async(request, runtime)

    def describe_flow_chart_with_options(
        self,
        request: waf_openapi_20211001_models.DescribeFlowChartRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeFlowChartResponse:
        """
        @summary Queries the traffic statistics of requests that are forwarded to Web Application Firewall (WAF).
        
        @param request: DescribeFlowChartRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeFlowChartResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_timestamp):
            query['EndTimestamp'] = request.end_timestamp
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource):
            query['Resource'] = request.resource
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.start_timestamp):
            query['StartTimestamp'] = request.start_timestamp
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeFlowChart',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeFlowChartResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_flow_chart_with_options_async(
        self,
        request: waf_openapi_20211001_models.DescribeFlowChartRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeFlowChartResponse:
        """
        @summary Queries the traffic statistics of requests that are forwarded to Web Application Firewall (WAF).
        
        @param request: DescribeFlowChartRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeFlowChartResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_timestamp):
            query['EndTimestamp'] = request.end_timestamp
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource):
            query['Resource'] = request.resource
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.start_timestamp):
            query['StartTimestamp'] = request.start_timestamp
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeFlowChart',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeFlowChartResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_flow_chart(
        self,
        request: waf_openapi_20211001_models.DescribeFlowChartRequest,
    ) -> waf_openapi_20211001_models.DescribeFlowChartResponse:
        """
        @summary Queries the traffic statistics of requests that are forwarded to Web Application Firewall (WAF).
        
        @param request: DescribeFlowChartRequest
        @return: DescribeFlowChartResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_flow_chart_with_options(request, runtime)

    async def describe_flow_chart_async(
        self,
        request: waf_openapi_20211001_models.DescribeFlowChartRequest,
    ) -> waf_openapi_20211001_models.DescribeFlowChartResponse:
        """
        @summary Queries the traffic statistics of requests that are forwarded to Web Application Firewall (WAF).
        
        @param request: DescribeFlowChartRequest
        @return: DescribeFlowChartResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_flow_chart_with_options_async(request, runtime)

    def describe_flow_top_resource_with_options(
        self,
        request: waf_openapi_20211001_models.DescribeFlowTopResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeFlowTopResourceResponse:
        """
        @summary Queries the top 10 protected objects that receive requests.
        
        @param request: DescribeFlowTopResourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeFlowTopResourceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_timestamp):
            query['EndTimestamp'] = request.end_timestamp
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.start_timestamp):
            query['StartTimestamp'] = request.start_timestamp
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeFlowTopResource',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeFlowTopResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_flow_top_resource_with_options_async(
        self,
        request: waf_openapi_20211001_models.DescribeFlowTopResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeFlowTopResourceResponse:
        """
        @summary Queries the top 10 protected objects that receive requests.
        
        @param request: DescribeFlowTopResourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeFlowTopResourceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_timestamp):
            query['EndTimestamp'] = request.end_timestamp
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.start_timestamp):
            query['StartTimestamp'] = request.start_timestamp
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeFlowTopResource',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeFlowTopResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_flow_top_resource(
        self,
        request: waf_openapi_20211001_models.DescribeFlowTopResourceRequest,
    ) -> waf_openapi_20211001_models.DescribeFlowTopResourceResponse:
        """
        @summary Queries the top 10 protected objects that receive requests.
        
        @param request: DescribeFlowTopResourceRequest
        @return: DescribeFlowTopResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_flow_top_resource_with_options(request, runtime)

    async def describe_flow_top_resource_async(
        self,
        request: waf_openapi_20211001_models.DescribeFlowTopResourceRequest,
    ) -> waf_openapi_20211001_models.DescribeFlowTopResourceResponse:
        """
        @summary Queries the top 10 protected objects that receive requests.
        
        @param request: DescribeFlowTopResourceRequest
        @return: DescribeFlowTopResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_flow_top_resource_with_options_async(request, runtime)

    def describe_flow_top_url_with_options(
        self,
        request: waf_openapi_20211001_models.DescribeFlowTopUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeFlowTopUrlResponse:
        """
        @summary Queries the top 10 URLs that are used to initiate requests.
        
        @param request: DescribeFlowTopUrlRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeFlowTopUrlResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_timestamp):
            query['EndTimestamp'] = request.end_timestamp
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource):
            query['Resource'] = request.resource
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.start_timestamp):
            query['StartTimestamp'] = request.start_timestamp
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeFlowTopUrl',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeFlowTopUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_flow_top_url_with_options_async(
        self,
        request: waf_openapi_20211001_models.DescribeFlowTopUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeFlowTopUrlResponse:
        """
        @summary Queries the top 10 URLs that are used to initiate requests.
        
        @param request: DescribeFlowTopUrlRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeFlowTopUrlResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_timestamp):
            query['EndTimestamp'] = request.end_timestamp
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource):
            query['Resource'] = request.resource
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.start_timestamp):
            query['StartTimestamp'] = request.start_timestamp
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeFlowTopUrl',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeFlowTopUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_flow_top_url(
        self,
        request: waf_openapi_20211001_models.DescribeFlowTopUrlRequest,
    ) -> waf_openapi_20211001_models.DescribeFlowTopUrlResponse:
        """
        @summary Queries the top 10 URLs that are used to initiate requests.
        
        @param request: DescribeFlowTopUrlRequest
        @return: DescribeFlowTopUrlResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_flow_top_url_with_options(request, runtime)

    async def describe_flow_top_url_async(
        self,
        request: waf_openapi_20211001_models.DescribeFlowTopUrlRequest,
    ) -> waf_openapi_20211001_models.DescribeFlowTopUrlResponse:
        """
        @summary Queries the top 10 URLs that are used to initiate requests.
        
        @param request: DescribeFlowTopUrlRequest
        @return: DescribeFlowTopUrlResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_flow_top_url_with_options_async(request, runtime)

    def describe_hybrid_cloud_groups_with_options(
        self,
        request: waf_openapi_20211001_models.DescribeHybridCloudGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeHybridCloudGroupsResponse:
        """
        @summary Queries the hybrid cloud node groups that are added to Web Application Firewall (WAF).
        
        @param request: DescribeHybridCloudGroupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeHybridCloudGroupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.cluster_proxy_type):
            query['ClusterProxyType'] = request.cluster_proxy_type
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.group_type):
            query['GroupType'] = request.group_type
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeHybridCloudGroups',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeHybridCloudGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_hybrid_cloud_groups_with_options_async(
        self,
        request: waf_openapi_20211001_models.DescribeHybridCloudGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeHybridCloudGroupsResponse:
        """
        @summary Queries the hybrid cloud node groups that are added to Web Application Firewall (WAF).
        
        @param request: DescribeHybridCloudGroupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeHybridCloudGroupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.cluster_proxy_type):
            query['ClusterProxyType'] = request.cluster_proxy_type
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.group_type):
            query['GroupType'] = request.group_type
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeHybridCloudGroups',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeHybridCloudGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_hybrid_cloud_groups(
        self,
        request: waf_openapi_20211001_models.DescribeHybridCloudGroupsRequest,
    ) -> waf_openapi_20211001_models.DescribeHybridCloudGroupsResponse:
        """
        @summary Queries the hybrid cloud node groups that are added to Web Application Firewall (WAF).
        
        @param request: DescribeHybridCloudGroupsRequest
        @return: DescribeHybridCloudGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_hybrid_cloud_groups_with_options(request, runtime)

    async def describe_hybrid_cloud_groups_async(
        self,
        request: waf_openapi_20211001_models.DescribeHybridCloudGroupsRequest,
    ) -> waf_openapi_20211001_models.DescribeHybridCloudGroupsResponse:
        """
        @summary Queries the hybrid cloud node groups that are added to Web Application Firewall (WAF).
        
        @param request: DescribeHybridCloudGroupsRequest
        @return: DescribeHybridCloudGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_hybrid_cloud_groups_with_options_async(request, runtime)

    def describe_hybrid_cloud_resources_with_options(
        self,
        request: waf_openapi_20211001_models.DescribeHybridCloudResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeHybridCloudResourcesResponse:
        """
        @summary Queries the domain names that are added to a Web Application Firewall (WAF) instance in hybrid cloud mode.
        
        @param request: DescribeHybridCloudResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeHybridCloudResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backend):
            query['Backend'] = request.backend
        if not UtilClient.is_unset(request.cname_enabled):
            query['CnameEnabled'] = request.cname_enabled
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeHybridCloudResources',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeHybridCloudResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_hybrid_cloud_resources_with_options_async(
        self,
        request: waf_openapi_20211001_models.DescribeHybridCloudResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeHybridCloudResourcesResponse:
        """
        @summary Queries the domain names that are added to a Web Application Firewall (WAF) instance in hybrid cloud mode.
        
        @param request: DescribeHybridCloudResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeHybridCloudResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backend):
            query['Backend'] = request.backend
        if not UtilClient.is_unset(request.cname_enabled):
            query['CnameEnabled'] = request.cname_enabled
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeHybridCloudResources',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeHybridCloudResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_hybrid_cloud_resources(
        self,
        request: waf_openapi_20211001_models.DescribeHybridCloudResourcesRequest,
    ) -> waf_openapi_20211001_models.DescribeHybridCloudResourcesResponse:
        """
        @summary Queries the domain names that are added to a Web Application Firewall (WAF) instance in hybrid cloud mode.
        
        @param request: DescribeHybridCloudResourcesRequest
        @return: DescribeHybridCloudResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_hybrid_cloud_resources_with_options(request, runtime)

    async def describe_hybrid_cloud_resources_async(
        self,
        request: waf_openapi_20211001_models.DescribeHybridCloudResourcesRequest,
    ) -> waf_openapi_20211001_models.DescribeHybridCloudResourcesResponse:
        """
        @summary Queries the domain names that are added to a Web Application Firewall (WAF) instance in hybrid cloud mode.
        
        @param request: DescribeHybridCloudResourcesRequest
        @return: DescribeHybridCloudResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_hybrid_cloud_resources_with_options_async(request, runtime)

    def describe_hybrid_cloud_user_with_options(
        self,
        request: waf_openapi_20211001_models.DescribeHybridCloudUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeHybridCloudUserResponse:
        """
        @summary Queries the HTTP and HTTPS ports that you can use when you add a domain name to Web Application Firewall (WAF) in hybrid cloud mode.
        
        @param request: DescribeHybridCloudUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeHybridCloudUserResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeHybridCloudUser',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeHybridCloudUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_hybrid_cloud_user_with_options_async(
        self,
        request: waf_openapi_20211001_models.DescribeHybridCloudUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeHybridCloudUserResponse:
        """
        @summary Queries the HTTP and HTTPS ports that you can use when you add a domain name to Web Application Firewall (WAF) in hybrid cloud mode.
        
        @param request: DescribeHybridCloudUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeHybridCloudUserResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeHybridCloudUser',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeHybridCloudUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_hybrid_cloud_user(
        self,
        request: waf_openapi_20211001_models.DescribeHybridCloudUserRequest,
    ) -> waf_openapi_20211001_models.DescribeHybridCloudUserResponse:
        """
        @summary Queries the HTTP and HTTPS ports that you can use when you add a domain name to Web Application Firewall (WAF) in hybrid cloud mode.
        
        @param request: DescribeHybridCloudUserRequest
        @return: DescribeHybridCloudUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_hybrid_cloud_user_with_options(request, runtime)

    async def describe_hybrid_cloud_user_async(
        self,
        request: waf_openapi_20211001_models.DescribeHybridCloudUserRequest,
    ) -> waf_openapi_20211001_models.DescribeHybridCloudUserResponse:
        """
        @summary Queries the HTTP and HTTPS ports that you can use when you add a domain name to Web Application Firewall (WAF) in hybrid cloud mode.
        
        @param request: DescribeHybridCloudUserRequest
        @return: DescribeHybridCloudUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_hybrid_cloud_user_with_options_async(request, runtime)

    def describe_instance_with_options(
        self,
        request: waf_openapi_20211001_models.DescribeInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeInstanceResponse:
        """
        @summary Queries the details of a Web Application Firewall (WAF) instance within the current Alibaba Cloud account.
        
        @param request: DescribeInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstance',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instance_with_options_async(
        self,
        request: waf_openapi_20211001_models.DescribeInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeInstanceResponse:
        """
        @summary Queries the details of a Web Application Firewall (WAF) instance within the current Alibaba Cloud account.
        
        @param request: DescribeInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstance',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_instance(
        self,
        request: waf_openapi_20211001_models.DescribeInstanceRequest,
    ) -> waf_openapi_20211001_models.DescribeInstanceResponse:
        """
        @summary Queries the details of a Web Application Firewall (WAF) instance within the current Alibaba Cloud account.
        
        @param request: DescribeInstanceRequest
        @return: DescribeInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_with_options(request, runtime)

    async def describe_instance_async(
        self,
        request: waf_openapi_20211001_models.DescribeInstanceRequest,
    ) -> waf_openapi_20211001_models.DescribeInstanceResponse:
        """
        @summary Queries the details of a Web Application Firewall (WAF) instance within the current Alibaba Cloud account.
        
        @param request: DescribeInstanceRequest
        @return: DescribeInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_instance_with_options_async(request, runtime)

    def describe_major_protection_black_ips_with_options(
        self,
        request: waf_openapi_20211001_models.DescribeMajorProtectionBlackIpsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeMajorProtectionBlackIpsResponse:
        """
        @summary Queries IP addresses in an IP address blacklist for major event protection by page.
        
        @param request: DescribeMajorProtectionBlackIpsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeMajorProtectionBlackIpsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.ip_like):
            query['IpLike'] = request.ip_like
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMajorProtectionBlackIps',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeMajorProtectionBlackIpsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_major_protection_black_ips_with_options_async(
        self,
        request: waf_openapi_20211001_models.DescribeMajorProtectionBlackIpsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeMajorProtectionBlackIpsResponse:
        """
        @summary Queries IP addresses in an IP address blacklist for major event protection by page.
        
        @param request: DescribeMajorProtectionBlackIpsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeMajorProtectionBlackIpsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.ip_like):
            query['IpLike'] = request.ip_like
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMajorProtectionBlackIps',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeMajorProtectionBlackIpsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_major_protection_black_ips(
        self,
        request: waf_openapi_20211001_models.DescribeMajorProtectionBlackIpsRequest,
    ) -> waf_openapi_20211001_models.DescribeMajorProtectionBlackIpsResponse:
        """
        @summary Queries IP addresses in an IP address blacklist for major event protection by page.
        
        @param request: DescribeMajorProtectionBlackIpsRequest
        @return: DescribeMajorProtectionBlackIpsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_major_protection_black_ips_with_options(request, runtime)

    async def describe_major_protection_black_ips_async(
        self,
        request: waf_openapi_20211001_models.DescribeMajorProtectionBlackIpsRequest,
    ) -> waf_openapi_20211001_models.DescribeMajorProtectionBlackIpsResponse:
        """
        @summary Queries IP addresses in an IP address blacklist for major event protection by page.
        
        @param request: DescribeMajorProtectionBlackIpsRequest
        @return: DescribeMajorProtectionBlackIpsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_major_protection_black_ips_with_options_async(request, runtime)

    def describe_member_accounts_with_options(
        self,
        request: waf_openapi_20211001_models.DescribeMemberAccountsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeMemberAccountsResponse:
        """
        @summary Queries information about members.
        
        @param request: DescribeMemberAccountsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeMemberAccountsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_status):
            query['AccountStatus'] = request.account_status
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMemberAccounts',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeMemberAccountsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_member_accounts_with_options_async(
        self,
        request: waf_openapi_20211001_models.DescribeMemberAccountsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeMemberAccountsResponse:
        """
        @summary Queries information about members.
        
        @param request: DescribeMemberAccountsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeMemberAccountsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_status):
            query['AccountStatus'] = request.account_status
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMemberAccounts',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeMemberAccountsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_member_accounts(
        self,
        request: waf_openapi_20211001_models.DescribeMemberAccountsRequest,
    ) -> waf_openapi_20211001_models.DescribeMemberAccountsResponse:
        """
        @summary Queries information about members.
        
        @param request: DescribeMemberAccountsRequest
        @return: DescribeMemberAccountsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_member_accounts_with_options(request, runtime)

    async def describe_member_accounts_async(
        self,
        request: waf_openapi_20211001_models.DescribeMemberAccountsRequest,
    ) -> waf_openapi_20211001_models.DescribeMemberAccountsResponse:
        """
        @summary Queries information about members.
        
        @param request: DescribeMemberAccountsRequest
        @return: DescribeMemberAccountsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_member_accounts_with_options_async(request, runtime)

    def describe_peak_trend_with_options(
        self,
        request: waf_openapi_20211001_models.DescribePeakTrendRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribePeakTrendResponse:
        """
        @summary Queries the queries per second (QPS) statistics of a WAF instance.
        
        @param request: DescribePeakTrendRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePeakTrendResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_timestamp):
            query['EndTimestamp'] = request.end_timestamp
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource):
            query['Resource'] = request.resource
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.start_timestamp):
            query['StartTimestamp'] = request.start_timestamp
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePeakTrend',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribePeakTrendResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_peak_trend_with_options_async(
        self,
        request: waf_openapi_20211001_models.DescribePeakTrendRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribePeakTrendResponse:
        """
        @summary Queries the queries per second (QPS) statistics of a WAF instance.
        
        @param request: DescribePeakTrendRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePeakTrendResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_timestamp):
            query['EndTimestamp'] = request.end_timestamp
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource):
            query['Resource'] = request.resource
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.start_timestamp):
            query['StartTimestamp'] = request.start_timestamp
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePeakTrend',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribePeakTrendResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_peak_trend(
        self,
        request: waf_openapi_20211001_models.DescribePeakTrendRequest,
    ) -> waf_openapi_20211001_models.DescribePeakTrendResponse:
        """
        @summary Queries the queries per second (QPS) statistics of a WAF instance.
        
        @param request: DescribePeakTrendRequest
        @return: DescribePeakTrendResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_peak_trend_with_options(request, runtime)

    async def describe_peak_trend_async(
        self,
        request: waf_openapi_20211001_models.DescribePeakTrendRequest,
    ) -> waf_openapi_20211001_models.DescribePeakTrendResponse:
        """
        @summary Queries the queries per second (QPS) statistics of a WAF instance.
        
        @param request: DescribePeakTrendRequest
        @return: DescribePeakTrendResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_peak_trend_with_options_async(request, runtime)

    def describe_product_instances_with_options(
        self,
        request: waf_openapi_20211001_models.DescribeProductInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeProductInstancesResponse:
        """
        @summary Queries the cloud service instances to be added to Web Application Firewall (WAF) in transparent proxy mode.
        
        @param request: DescribeProductInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeProductInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_user_id):
            query['OwnerUserId'] = request.owner_user_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_instance_id):
            query['ResourceInstanceId'] = request.resource_instance_id
        if not UtilClient.is_unset(request.resource_ip):
            query['ResourceIp'] = request.resource_ip
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.resource_name):
            query['ResourceName'] = request.resource_name
        if not UtilClient.is_unset(request.resource_product):
            query['ResourceProduct'] = request.resource_product
        if not UtilClient.is_unset(request.resource_region_id):
            query['ResourceRegionId'] = request.resource_region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeProductInstances',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeProductInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_product_instances_with_options_async(
        self,
        request: waf_openapi_20211001_models.DescribeProductInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeProductInstancesResponse:
        """
        @summary Queries the cloud service instances to be added to Web Application Firewall (WAF) in transparent proxy mode.
        
        @param request: DescribeProductInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeProductInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_user_id):
            query['OwnerUserId'] = request.owner_user_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_instance_id):
            query['ResourceInstanceId'] = request.resource_instance_id
        if not UtilClient.is_unset(request.resource_ip):
            query['ResourceIp'] = request.resource_ip
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.resource_name):
            query['ResourceName'] = request.resource_name
        if not UtilClient.is_unset(request.resource_product):
            query['ResourceProduct'] = request.resource_product
        if not UtilClient.is_unset(request.resource_region_id):
            query['ResourceRegionId'] = request.resource_region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeProductInstances',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeProductInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_product_instances(
        self,
        request: waf_openapi_20211001_models.DescribeProductInstancesRequest,
    ) -> waf_openapi_20211001_models.DescribeProductInstancesResponse:
        """
        @summary Queries the cloud service instances to be added to Web Application Firewall (WAF) in transparent proxy mode.
        
        @param request: DescribeProductInstancesRequest
        @return: DescribeProductInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_product_instances_with_options(request, runtime)

    async def describe_product_instances_async(
        self,
        request: waf_openapi_20211001_models.DescribeProductInstancesRequest,
    ) -> waf_openapi_20211001_models.DescribeProductInstancesResponse:
        """
        @summary Queries the cloud service instances to be added to Web Application Firewall (WAF) in transparent proxy mode.
        
        @param request: DescribeProductInstancesRequest
        @return: DescribeProductInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_product_instances_with_options_async(request, runtime)

    def describe_punished_domains_with_options(
        self,
        request: waf_openapi_20211001_models.DescribePunishedDomainsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribePunishedDomainsResponse:
        """
        @summary Queries a list of domain names that are added to Web Application Firewall (WAF) and penalized for failing to obtain an Internet Content Provider (ICP) filing.
        
        @param request: DescribePunishedDomainsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePunishedDomainsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domains):
            query['Domains'] = request.domains
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePunishedDomains',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribePunishedDomainsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_punished_domains_with_options_async(
        self,
        request: waf_openapi_20211001_models.DescribePunishedDomainsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribePunishedDomainsResponse:
        """
        @summary Queries a list of domain names that are added to Web Application Firewall (WAF) and penalized for failing to obtain an Internet Content Provider (ICP) filing.
        
        @param request: DescribePunishedDomainsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePunishedDomainsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domains):
            query['Domains'] = request.domains
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePunishedDomains',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribePunishedDomainsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_punished_domains(
        self,
        request: waf_openapi_20211001_models.DescribePunishedDomainsRequest,
    ) -> waf_openapi_20211001_models.DescribePunishedDomainsResponse:
        """
        @summary Queries a list of domain names that are added to Web Application Firewall (WAF) and penalized for failing to obtain an Internet Content Provider (ICP) filing.
        
        @param request: DescribePunishedDomainsRequest
        @return: DescribePunishedDomainsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_punished_domains_with_options(request, runtime)

    async def describe_punished_domains_async(
        self,
        request: waf_openapi_20211001_models.DescribePunishedDomainsRequest,
    ) -> waf_openapi_20211001_models.DescribePunishedDomainsResponse:
        """
        @summary Queries a list of domain names that are added to Web Application Firewall (WAF) and penalized for failing to obtain an Internet Content Provider (ICP) filing.
        
        @param request: DescribePunishedDomainsRequest
        @return: DescribePunishedDomainsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_punished_domains_with_options_async(request, runtime)

    def describe_resource_instance_certs_with_options(
        self,
        request: waf_openapi_20211001_models.DescribeResourceInstanceCertsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeResourceInstanceCertsResponse:
        """
        @summary Queries the certificates that are used in cloud service instances. The certificates returned include the certificates within the delegated administrator account and the certificates within members to which specific instances belong. For example, the delegated administrator account has certificate 1, instance lb-xx-1 belongs to member B, and member B has certificate 2. If you specify instance lb-xx-1 in the request, certificate 1 and certificate 2 are returned.
        
        @param request: DescribeResourceInstanceCertsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeResourceInstanceCertsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_instance_id):
            query['ResourceInstanceId'] = request.resource_instance_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeResourceInstanceCerts',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeResourceInstanceCertsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_resource_instance_certs_with_options_async(
        self,
        request: waf_openapi_20211001_models.DescribeResourceInstanceCertsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeResourceInstanceCertsResponse:
        """
        @summary Queries the certificates that are used in cloud service instances. The certificates returned include the certificates within the delegated administrator account and the certificates within members to which specific instances belong. For example, the delegated administrator account has certificate 1, instance lb-xx-1 belongs to member B, and member B has certificate 2. If you specify instance lb-xx-1 in the request, certificate 1 and certificate 2 are returned.
        
        @param request: DescribeResourceInstanceCertsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeResourceInstanceCertsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_instance_id):
            query['ResourceInstanceId'] = request.resource_instance_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeResourceInstanceCerts',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeResourceInstanceCertsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_resource_instance_certs(
        self,
        request: waf_openapi_20211001_models.DescribeResourceInstanceCertsRequest,
    ) -> waf_openapi_20211001_models.DescribeResourceInstanceCertsResponse:
        """
        @summary Queries the certificates that are used in cloud service instances. The certificates returned include the certificates within the delegated administrator account and the certificates within members to which specific instances belong. For example, the delegated administrator account has certificate 1, instance lb-xx-1 belongs to member B, and member B has certificate 2. If you specify instance lb-xx-1 in the request, certificate 1 and certificate 2 are returned.
        
        @param request: DescribeResourceInstanceCertsRequest
        @return: DescribeResourceInstanceCertsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_resource_instance_certs_with_options(request, runtime)

    async def describe_resource_instance_certs_async(
        self,
        request: waf_openapi_20211001_models.DescribeResourceInstanceCertsRequest,
    ) -> waf_openapi_20211001_models.DescribeResourceInstanceCertsResponse:
        """
        @summary Queries the certificates that are used in cloud service instances. The certificates returned include the certificates within the delegated administrator account and the certificates within members to which specific instances belong. For example, the delegated administrator account has certificate 1, instance lb-xx-1 belongs to member B, and member B has certificate 2. If you specify instance lb-xx-1 in the request, certificate 1 and certificate 2 are returned.
        
        @param request: DescribeResourceInstanceCertsRequest
        @return: DescribeResourceInstanceCertsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_resource_instance_certs_with_options_async(request, runtime)

    def describe_resource_log_status_with_options(
        self,
        request: waf_openapi_20211001_models.DescribeResourceLogStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeResourceLogStatusResponse:
        """
        @summary Queries whether the log collection feature is enabled for a protected object.
        
        @param request: DescribeResourceLogStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeResourceLogStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.resources):
            query['Resources'] = request.resources
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeResourceLogStatus',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeResourceLogStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_resource_log_status_with_options_async(
        self,
        request: waf_openapi_20211001_models.DescribeResourceLogStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeResourceLogStatusResponse:
        """
        @summary Queries whether the log collection feature is enabled for a protected object.
        
        @param request: DescribeResourceLogStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeResourceLogStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.resources):
            query['Resources'] = request.resources
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeResourceLogStatus',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeResourceLogStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_resource_log_status(
        self,
        request: waf_openapi_20211001_models.DescribeResourceLogStatusRequest,
    ) -> waf_openapi_20211001_models.DescribeResourceLogStatusResponse:
        """
        @summary Queries whether the log collection feature is enabled for a protected object.
        
        @param request: DescribeResourceLogStatusRequest
        @return: DescribeResourceLogStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_resource_log_status_with_options(request, runtime)

    async def describe_resource_log_status_async(
        self,
        request: waf_openapi_20211001_models.DescribeResourceLogStatusRequest,
    ) -> waf_openapi_20211001_models.DescribeResourceLogStatusResponse:
        """
        @summary Queries whether the log collection feature is enabled for a protected object.
        
        @param request: DescribeResourceLogStatusRequest
        @return: DescribeResourceLogStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_resource_log_status_with_options_async(request, runtime)

    def describe_resource_port_with_options(
        self,
        request: waf_openapi_20211001_models.DescribeResourcePortRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeResourcePortResponse:
        """
        @summary Queries the ports of a cloud service instance that are added to Web Application Firewall (WAF).
        
        @param request: DescribeResourcePortRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeResourcePortResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_instance_id):
            query['ResourceInstanceId'] = request.resource_instance_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeResourcePort',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeResourcePortResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_resource_port_with_options_async(
        self,
        request: waf_openapi_20211001_models.DescribeResourcePortRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeResourcePortResponse:
        """
        @summary Queries the ports of a cloud service instance that are added to Web Application Firewall (WAF).
        
        @param request: DescribeResourcePortRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeResourcePortResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_instance_id):
            query['ResourceInstanceId'] = request.resource_instance_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeResourcePort',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeResourcePortResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_resource_port(
        self,
        request: waf_openapi_20211001_models.DescribeResourcePortRequest,
    ) -> waf_openapi_20211001_models.DescribeResourcePortResponse:
        """
        @summary Queries the ports of a cloud service instance that are added to Web Application Firewall (WAF).
        
        @param request: DescribeResourcePortRequest
        @return: DescribeResourcePortResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_resource_port_with_options(request, runtime)

    async def describe_resource_port_async(
        self,
        request: waf_openapi_20211001_models.DescribeResourcePortRequest,
    ) -> waf_openapi_20211001_models.DescribeResourcePortResponse:
        """
        @summary Queries the ports of a cloud service instance that are added to Web Application Firewall (WAF).
        
        @param request: DescribeResourcePortRequest
        @return: DescribeResourcePortResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_resource_port_with_options_async(request, runtime)

    def describe_resource_region_id_with_options(
        self,
        request: waf_openapi_20211001_models.DescribeResourceRegionIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeResourceRegionIdResponse:
        """
        @summary Queries the region IDs of the resources that are added to Web Application Firewall (WAF) in cloud native mode. The resources include Application Load Balancer (ALB) instances, Microservices Engine (MSE) instances, and custom domain names bound to web applications in Function Compute.
        
        @param request: DescribeResourceRegionIdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeResourceRegionIdResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeResourceRegionId',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeResourceRegionIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_resource_region_id_with_options_async(
        self,
        request: waf_openapi_20211001_models.DescribeResourceRegionIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeResourceRegionIdResponse:
        """
        @summary Queries the region IDs of the resources that are added to Web Application Firewall (WAF) in cloud native mode. The resources include Application Load Balancer (ALB) instances, Microservices Engine (MSE) instances, and custom domain names bound to web applications in Function Compute.
        
        @param request: DescribeResourceRegionIdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeResourceRegionIdResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeResourceRegionId',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeResourceRegionIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_resource_region_id(
        self,
        request: waf_openapi_20211001_models.DescribeResourceRegionIdRequest,
    ) -> waf_openapi_20211001_models.DescribeResourceRegionIdResponse:
        """
        @summary Queries the region IDs of the resources that are added to Web Application Firewall (WAF) in cloud native mode. The resources include Application Load Balancer (ALB) instances, Microservices Engine (MSE) instances, and custom domain names bound to web applications in Function Compute.
        
        @param request: DescribeResourceRegionIdRequest
        @return: DescribeResourceRegionIdResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_resource_region_id_with_options(request, runtime)

    async def describe_resource_region_id_async(
        self,
        request: waf_openapi_20211001_models.DescribeResourceRegionIdRequest,
    ) -> waf_openapi_20211001_models.DescribeResourceRegionIdResponse:
        """
        @summary Queries the region IDs of the resources that are added to Web Application Firewall (WAF) in cloud native mode. The resources include Application Load Balancer (ALB) instances, Microservices Engine (MSE) instances, and custom domain names bound to web applications in Function Compute.
        
        @param request: DescribeResourceRegionIdRequest
        @return: DescribeResourceRegionIdResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_resource_region_id_with_options_async(request, runtime)

    def describe_resource_support_regions_with_options(
        self,
        request: waf_openapi_20211001_models.DescribeResourceSupportRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeResourceSupportRegionsResponse:
        """
        @summary Queries the region IDs of Classic Load Balancer (CLB) and Elastic Compute Service (ECS) instances that can be added to Web Application Firewall (WAF) in transparent proxy mode.
        
        @param request: DescribeResourceSupportRegionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeResourceSupportRegionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeResourceSupportRegions',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeResourceSupportRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_resource_support_regions_with_options_async(
        self,
        request: waf_openapi_20211001_models.DescribeResourceSupportRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeResourceSupportRegionsResponse:
        """
        @summary Queries the region IDs of Classic Load Balancer (CLB) and Elastic Compute Service (ECS) instances that can be added to Web Application Firewall (WAF) in transparent proxy mode.
        
        @param request: DescribeResourceSupportRegionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeResourceSupportRegionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeResourceSupportRegions',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeResourceSupportRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_resource_support_regions(
        self,
        request: waf_openapi_20211001_models.DescribeResourceSupportRegionsRequest,
    ) -> waf_openapi_20211001_models.DescribeResourceSupportRegionsResponse:
        """
        @summary Queries the region IDs of Classic Load Balancer (CLB) and Elastic Compute Service (ECS) instances that can be added to Web Application Firewall (WAF) in transparent proxy mode.
        
        @param request: DescribeResourceSupportRegionsRequest
        @return: DescribeResourceSupportRegionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_resource_support_regions_with_options(request, runtime)

    async def describe_resource_support_regions_async(
        self,
        request: waf_openapi_20211001_models.DescribeResourceSupportRegionsRequest,
    ) -> waf_openapi_20211001_models.DescribeResourceSupportRegionsResponse:
        """
        @summary Queries the region IDs of Classic Load Balancer (CLB) and Elastic Compute Service (ECS) instances that can be added to Web Application Firewall (WAF) in transparent proxy mode.
        
        @param request: DescribeResourceSupportRegionsRequest
        @return: DescribeResourceSupportRegionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_resource_support_regions_with_options_async(request, runtime)

    def describe_response_code_trend_graph_with_options(
        self,
        request: waf_openapi_20211001_models.DescribeResponseCodeTrendGraphRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeResponseCodeTrendGraphResponse:
        """
        @summary Queries the trend of the number of error codes that are returned to clients or Web Application Firewall (WAF). The error codes include 302, 405, 444, 499, and 5XX.
        
        @param request: DescribeResponseCodeTrendGraphRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeResponseCodeTrendGraphResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_timestamp):
            query['EndTimestamp'] = request.end_timestamp
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource):
            query['Resource'] = request.resource
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.start_timestamp):
            query['StartTimestamp'] = request.start_timestamp
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeResponseCodeTrendGraph',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeResponseCodeTrendGraphResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_response_code_trend_graph_with_options_async(
        self,
        request: waf_openapi_20211001_models.DescribeResponseCodeTrendGraphRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeResponseCodeTrendGraphResponse:
        """
        @summary Queries the trend of the number of error codes that are returned to clients or Web Application Firewall (WAF). The error codes include 302, 405, 444, 499, and 5XX.
        
        @param request: DescribeResponseCodeTrendGraphRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeResponseCodeTrendGraphResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_timestamp):
            query['EndTimestamp'] = request.end_timestamp
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource):
            query['Resource'] = request.resource
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.start_timestamp):
            query['StartTimestamp'] = request.start_timestamp
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeResponseCodeTrendGraph',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeResponseCodeTrendGraphResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_response_code_trend_graph(
        self,
        request: waf_openapi_20211001_models.DescribeResponseCodeTrendGraphRequest,
    ) -> waf_openapi_20211001_models.DescribeResponseCodeTrendGraphResponse:
        """
        @summary Queries the trend of the number of error codes that are returned to clients or Web Application Firewall (WAF). The error codes include 302, 405, 444, 499, and 5XX.
        
        @param request: DescribeResponseCodeTrendGraphRequest
        @return: DescribeResponseCodeTrendGraphResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_response_code_trend_graph_with_options(request, runtime)

    async def describe_response_code_trend_graph_async(
        self,
        request: waf_openapi_20211001_models.DescribeResponseCodeTrendGraphRequest,
    ) -> waf_openapi_20211001_models.DescribeResponseCodeTrendGraphResponse:
        """
        @summary Queries the trend of the number of error codes that are returned to clients or Web Application Firewall (WAF). The error codes include 302, 405, 444, 499, and 5XX.
        
        @param request: DescribeResponseCodeTrendGraphRequest
        @return: DescribeResponseCodeTrendGraphResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_response_code_trend_graph_with_options_async(request, runtime)

    def describe_rule_groups_with_options(
        self,
        request: waf_openapi_20211001_models.DescribeRuleGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeRuleGroupsResponse:
        """
        @summary Queries regular expression rule groups by page.
        
        @param request: DescribeRuleGroupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRuleGroupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.search_type):
            query['SearchType'] = request.search_type
        if not UtilClient.is_unset(request.search_value):
            query['SearchValue'] = request.search_value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRuleGroups',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeRuleGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_rule_groups_with_options_async(
        self,
        request: waf_openapi_20211001_models.DescribeRuleGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeRuleGroupsResponse:
        """
        @summary Queries regular expression rule groups by page.
        
        @param request: DescribeRuleGroupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRuleGroupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.search_type):
            query['SearchType'] = request.search_type
        if not UtilClient.is_unset(request.search_value):
            query['SearchValue'] = request.search_value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRuleGroups',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeRuleGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_rule_groups(
        self,
        request: waf_openapi_20211001_models.DescribeRuleGroupsRequest,
    ) -> waf_openapi_20211001_models.DescribeRuleGroupsResponse:
        """
        @summary Queries regular expression rule groups by page.
        
        @param request: DescribeRuleGroupsRequest
        @return: DescribeRuleGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_rule_groups_with_options(request, runtime)

    async def describe_rule_groups_async(
        self,
        request: waf_openapi_20211001_models.DescribeRuleGroupsRequest,
    ) -> waf_openapi_20211001_models.DescribeRuleGroupsResponse:
        """
        @summary Queries regular expression rule groups by page.
        
        @param request: DescribeRuleGroupsRequest
        @return: DescribeRuleGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_rule_groups_with_options_async(request, runtime)

    def describe_rule_hits_top_client_ip_with_options(
        self,
        request: waf_openapi_20211001_models.DescribeRuleHitsTopClientIpRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeRuleHitsTopClientIpResponse:
        """
        @summary Queries the top 10 IP addresses from which attacks are initiated.
        
        @param request: DescribeRuleHitsTopClientIpRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRuleHitsTopClientIpResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_timestamp):
            query['EndTimestamp'] = request.end_timestamp
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource):
            query['Resource'] = request.resource
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.rule_type):
            query['RuleType'] = request.rule_type
        if not UtilClient.is_unset(request.start_timestamp):
            query['StartTimestamp'] = request.start_timestamp
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRuleHitsTopClientIp',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeRuleHitsTopClientIpResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_rule_hits_top_client_ip_with_options_async(
        self,
        request: waf_openapi_20211001_models.DescribeRuleHitsTopClientIpRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeRuleHitsTopClientIpResponse:
        """
        @summary Queries the top 10 IP addresses from which attacks are initiated.
        
        @param request: DescribeRuleHitsTopClientIpRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRuleHitsTopClientIpResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_timestamp):
            query['EndTimestamp'] = request.end_timestamp
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource):
            query['Resource'] = request.resource
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.rule_type):
            query['RuleType'] = request.rule_type
        if not UtilClient.is_unset(request.start_timestamp):
            query['StartTimestamp'] = request.start_timestamp
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRuleHitsTopClientIp',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeRuleHitsTopClientIpResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_rule_hits_top_client_ip(
        self,
        request: waf_openapi_20211001_models.DescribeRuleHitsTopClientIpRequest,
    ) -> waf_openapi_20211001_models.DescribeRuleHitsTopClientIpResponse:
        """
        @summary Queries the top 10 IP addresses from which attacks are initiated.
        
        @param request: DescribeRuleHitsTopClientIpRequest
        @return: DescribeRuleHitsTopClientIpResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_rule_hits_top_client_ip_with_options(request, runtime)

    async def describe_rule_hits_top_client_ip_async(
        self,
        request: waf_openapi_20211001_models.DescribeRuleHitsTopClientIpRequest,
    ) -> waf_openapi_20211001_models.DescribeRuleHitsTopClientIpResponse:
        """
        @summary Queries the top 10 IP addresses from which attacks are initiated.
        
        @param request: DescribeRuleHitsTopClientIpRequest
        @return: DescribeRuleHitsTopClientIpResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_rule_hits_top_client_ip_with_options_async(request, runtime)

    def describe_rule_hits_top_resource_with_options(
        self,
        request: waf_openapi_20211001_models.DescribeRuleHitsTopResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeRuleHitsTopResourceResponse:
        """
        @summary Queries the top 10 protected objects that trigger protection rules.
        
        @param request: DescribeRuleHitsTopResourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRuleHitsTopResourceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_timestamp):
            query['EndTimestamp'] = request.end_timestamp
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.rule_type):
            query['RuleType'] = request.rule_type
        if not UtilClient.is_unset(request.start_timestamp):
            query['StartTimestamp'] = request.start_timestamp
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRuleHitsTopResource',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeRuleHitsTopResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_rule_hits_top_resource_with_options_async(
        self,
        request: waf_openapi_20211001_models.DescribeRuleHitsTopResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeRuleHitsTopResourceResponse:
        """
        @summary Queries the top 10 protected objects that trigger protection rules.
        
        @param request: DescribeRuleHitsTopResourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRuleHitsTopResourceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_timestamp):
            query['EndTimestamp'] = request.end_timestamp
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.rule_type):
            query['RuleType'] = request.rule_type
        if not UtilClient.is_unset(request.start_timestamp):
            query['StartTimestamp'] = request.start_timestamp
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRuleHitsTopResource',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeRuleHitsTopResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_rule_hits_top_resource(
        self,
        request: waf_openapi_20211001_models.DescribeRuleHitsTopResourceRequest,
    ) -> waf_openapi_20211001_models.DescribeRuleHitsTopResourceResponse:
        """
        @summary Queries the top 10 protected objects that trigger protection rules.
        
        @param request: DescribeRuleHitsTopResourceRequest
        @return: DescribeRuleHitsTopResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_rule_hits_top_resource_with_options(request, runtime)

    async def describe_rule_hits_top_resource_async(
        self,
        request: waf_openapi_20211001_models.DescribeRuleHitsTopResourceRequest,
    ) -> waf_openapi_20211001_models.DescribeRuleHitsTopResourceResponse:
        """
        @summary Queries the top 10 protected objects that trigger protection rules.
        
        @param request: DescribeRuleHitsTopResourceRequest
        @return: DescribeRuleHitsTopResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_rule_hits_top_resource_with_options_async(request, runtime)

    def describe_rule_hits_top_rule_id_with_options(
        self,
        request: waf_openapi_20211001_models.DescribeRuleHitsTopRuleIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeRuleHitsTopRuleIdResponse:
        """
        @summary Queries the IDs of the top 10 protection rules that are matched by requests.
        
        @param request: DescribeRuleHitsTopRuleIdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRuleHitsTopRuleIdResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_timestamp):
            query['EndTimestamp'] = request.end_timestamp
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.is_group_resource):
            query['IsGroupResource'] = request.is_group_resource
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource):
            query['Resource'] = request.resource
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.rule_type):
            query['RuleType'] = request.rule_type
        if not UtilClient.is_unset(request.start_timestamp):
            query['StartTimestamp'] = request.start_timestamp
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRuleHitsTopRuleId',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeRuleHitsTopRuleIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_rule_hits_top_rule_id_with_options_async(
        self,
        request: waf_openapi_20211001_models.DescribeRuleHitsTopRuleIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeRuleHitsTopRuleIdResponse:
        """
        @summary Queries the IDs of the top 10 protection rules that are matched by requests.
        
        @param request: DescribeRuleHitsTopRuleIdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRuleHitsTopRuleIdResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_timestamp):
            query['EndTimestamp'] = request.end_timestamp
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.is_group_resource):
            query['IsGroupResource'] = request.is_group_resource
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource):
            query['Resource'] = request.resource
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.rule_type):
            query['RuleType'] = request.rule_type
        if not UtilClient.is_unset(request.start_timestamp):
            query['StartTimestamp'] = request.start_timestamp
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRuleHitsTopRuleId',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeRuleHitsTopRuleIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_rule_hits_top_rule_id(
        self,
        request: waf_openapi_20211001_models.DescribeRuleHitsTopRuleIdRequest,
    ) -> waf_openapi_20211001_models.DescribeRuleHitsTopRuleIdResponse:
        """
        @summary Queries the IDs of the top 10 protection rules that are matched by requests.
        
        @param request: DescribeRuleHitsTopRuleIdRequest
        @return: DescribeRuleHitsTopRuleIdResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_rule_hits_top_rule_id_with_options(request, runtime)

    async def describe_rule_hits_top_rule_id_async(
        self,
        request: waf_openapi_20211001_models.DescribeRuleHitsTopRuleIdRequest,
    ) -> waf_openapi_20211001_models.DescribeRuleHitsTopRuleIdResponse:
        """
        @summary Queries the IDs of the top 10 protection rules that are matched by requests.
        
        @param request: DescribeRuleHitsTopRuleIdRequest
        @return: DescribeRuleHitsTopRuleIdResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_rule_hits_top_rule_id_with_options_async(request, runtime)

    def describe_rule_hits_top_tule_type_with_options(
        self,
        request: waf_openapi_20211001_models.DescribeRuleHitsTopTuleTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeRuleHitsTopTuleTypeResponse:
        """
        @summary Queries the top 10 protection modules that are matched.
        
        @param request: DescribeRuleHitsTopTuleTypeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRuleHitsTopTuleTypeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_timestamp):
            query['EndTimestamp'] = request.end_timestamp
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource):
            query['Resource'] = request.resource
        if not UtilClient.is_unset(request.start_timestamp):
            query['StartTimestamp'] = request.start_timestamp
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRuleHitsTopTuleType',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeRuleHitsTopTuleTypeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_rule_hits_top_tule_type_with_options_async(
        self,
        request: waf_openapi_20211001_models.DescribeRuleHitsTopTuleTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeRuleHitsTopTuleTypeResponse:
        """
        @summary Queries the top 10 protection modules that are matched.
        
        @param request: DescribeRuleHitsTopTuleTypeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRuleHitsTopTuleTypeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_timestamp):
            query['EndTimestamp'] = request.end_timestamp
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource):
            query['Resource'] = request.resource
        if not UtilClient.is_unset(request.start_timestamp):
            query['StartTimestamp'] = request.start_timestamp
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRuleHitsTopTuleType',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeRuleHitsTopTuleTypeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_rule_hits_top_tule_type(
        self,
        request: waf_openapi_20211001_models.DescribeRuleHitsTopTuleTypeRequest,
    ) -> waf_openapi_20211001_models.DescribeRuleHitsTopTuleTypeResponse:
        """
        @summary Queries the top 10 protection modules that are matched.
        
        @param request: DescribeRuleHitsTopTuleTypeRequest
        @return: DescribeRuleHitsTopTuleTypeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_rule_hits_top_tule_type_with_options(request, runtime)

    async def describe_rule_hits_top_tule_type_async(
        self,
        request: waf_openapi_20211001_models.DescribeRuleHitsTopTuleTypeRequest,
    ) -> waf_openapi_20211001_models.DescribeRuleHitsTopTuleTypeResponse:
        """
        @summary Queries the top 10 protection modules that are matched.
        
        @param request: DescribeRuleHitsTopTuleTypeRequest
        @return: DescribeRuleHitsTopTuleTypeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_rule_hits_top_tule_type_with_options_async(request, runtime)

    def describe_rule_hits_top_ua_with_options(
        self,
        request: waf_openapi_20211001_models.DescribeRuleHitsTopUaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeRuleHitsTopUaResponse:
        """
        @summary Queries the top 10 user agents that are used to initiate attacks.
        
        @param request: DescribeRuleHitsTopUaRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRuleHitsTopUaResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_timestamp):
            query['EndTimestamp'] = request.end_timestamp
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource):
            query['Resource'] = request.resource
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.start_timestamp):
            query['StartTimestamp'] = request.start_timestamp
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRuleHitsTopUa',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeRuleHitsTopUaResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_rule_hits_top_ua_with_options_async(
        self,
        request: waf_openapi_20211001_models.DescribeRuleHitsTopUaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeRuleHitsTopUaResponse:
        """
        @summary Queries the top 10 user agents that are used to initiate attacks.
        
        @param request: DescribeRuleHitsTopUaRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRuleHitsTopUaResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_timestamp):
            query['EndTimestamp'] = request.end_timestamp
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource):
            query['Resource'] = request.resource
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.start_timestamp):
            query['StartTimestamp'] = request.start_timestamp
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRuleHitsTopUa',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeRuleHitsTopUaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_rule_hits_top_ua(
        self,
        request: waf_openapi_20211001_models.DescribeRuleHitsTopUaRequest,
    ) -> waf_openapi_20211001_models.DescribeRuleHitsTopUaResponse:
        """
        @summary Queries the top 10 user agents that are used to initiate attacks.
        
        @param request: DescribeRuleHitsTopUaRequest
        @return: DescribeRuleHitsTopUaResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_rule_hits_top_ua_with_options(request, runtime)

    async def describe_rule_hits_top_ua_async(
        self,
        request: waf_openapi_20211001_models.DescribeRuleHitsTopUaRequest,
    ) -> waf_openapi_20211001_models.DescribeRuleHitsTopUaResponse:
        """
        @summary Queries the top 10 user agents that are used to initiate attacks.
        
        @param request: DescribeRuleHitsTopUaRequest
        @return: DescribeRuleHitsTopUaResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_rule_hits_top_ua_with_options_async(request, runtime)

    def describe_rule_hits_top_url_with_options(
        self,
        request: waf_openapi_20211001_models.DescribeRuleHitsTopUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeRuleHitsTopUrlResponse:
        """
        @summary Queries the top 10 URLs that trigger protection rules.
        
        @param request: DescribeRuleHitsTopUrlRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRuleHitsTopUrlResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_timestamp):
            query['EndTimestamp'] = request.end_timestamp
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource):
            query['Resource'] = request.resource
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.rule_type):
            query['RuleType'] = request.rule_type
        if not UtilClient.is_unset(request.start_timestamp):
            query['StartTimestamp'] = request.start_timestamp
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRuleHitsTopUrl',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeRuleHitsTopUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_rule_hits_top_url_with_options_async(
        self,
        request: waf_openapi_20211001_models.DescribeRuleHitsTopUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeRuleHitsTopUrlResponse:
        """
        @summary Queries the top 10 URLs that trigger protection rules.
        
        @param request: DescribeRuleHitsTopUrlRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRuleHitsTopUrlResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_timestamp):
            query['EndTimestamp'] = request.end_timestamp
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource):
            query['Resource'] = request.resource
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.rule_type):
            query['RuleType'] = request.rule_type
        if not UtilClient.is_unset(request.start_timestamp):
            query['StartTimestamp'] = request.start_timestamp
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRuleHitsTopUrl',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeRuleHitsTopUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_rule_hits_top_url(
        self,
        request: waf_openapi_20211001_models.DescribeRuleHitsTopUrlRequest,
    ) -> waf_openapi_20211001_models.DescribeRuleHitsTopUrlResponse:
        """
        @summary Queries the top 10 URLs that trigger protection rules.
        
        @param request: DescribeRuleHitsTopUrlRequest
        @return: DescribeRuleHitsTopUrlResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_rule_hits_top_url_with_options(request, runtime)

    async def describe_rule_hits_top_url_async(
        self,
        request: waf_openapi_20211001_models.DescribeRuleHitsTopUrlRequest,
    ) -> waf_openapi_20211001_models.DescribeRuleHitsTopUrlResponse:
        """
        @summary Queries the top 10 URLs that trigger protection rules.
        
        @param request: DescribeRuleHitsTopUrlRequest
        @return: DescribeRuleHitsTopUrlResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_rule_hits_top_url_with_options_async(request, runtime)

    def describe_sls_auth_status_with_options(
        self,
        request: waf_openapi_20211001_models.DescribeSlsAuthStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeSlsAuthStatusResponse:
        """
        @summary Queries whether Web Application Firewall (WAF) is authorized to access Logstores.
        
        @param request: DescribeSlsAuthStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSlsAuthStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSlsAuthStatus',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeSlsAuthStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sls_auth_status_with_options_async(
        self,
        request: waf_openapi_20211001_models.DescribeSlsAuthStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeSlsAuthStatusResponse:
        """
        @summary Queries whether Web Application Firewall (WAF) is authorized to access Logstores.
        
        @param request: DescribeSlsAuthStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSlsAuthStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSlsAuthStatus',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeSlsAuthStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_sls_auth_status(
        self,
        request: waf_openapi_20211001_models.DescribeSlsAuthStatusRequest,
    ) -> waf_openapi_20211001_models.DescribeSlsAuthStatusResponse:
        """
        @summary Queries whether Web Application Firewall (WAF) is authorized to access Logstores.
        
        @param request: DescribeSlsAuthStatusRequest
        @return: DescribeSlsAuthStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_sls_auth_status_with_options(request, runtime)

    async def describe_sls_auth_status_async(
        self,
        request: waf_openapi_20211001_models.DescribeSlsAuthStatusRequest,
    ) -> waf_openapi_20211001_models.DescribeSlsAuthStatusResponse:
        """
        @summary Queries whether Web Application Firewall (WAF) is authorized to access Logstores.
        
        @param request: DescribeSlsAuthStatusRequest
        @return: DescribeSlsAuthStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_sls_auth_status_with_options_async(request, runtime)

    def describe_sls_log_store_with_options(
        self,
        request: waf_openapi_20211001_models.DescribeSlsLogStoreRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeSlsLogStoreResponse:
        """
        @summary Queries information about a Logstore, such as the total capacity, storage duration, and used capacity.
        
        @param request: DescribeSlsLogStoreRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSlsLogStoreResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSlsLogStore',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeSlsLogStoreResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sls_log_store_with_options_async(
        self,
        request: waf_openapi_20211001_models.DescribeSlsLogStoreRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeSlsLogStoreResponse:
        """
        @summary Queries information about a Logstore, such as the total capacity, storage duration, and used capacity.
        
        @param request: DescribeSlsLogStoreRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSlsLogStoreResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSlsLogStore',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeSlsLogStoreResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_sls_log_store(
        self,
        request: waf_openapi_20211001_models.DescribeSlsLogStoreRequest,
    ) -> waf_openapi_20211001_models.DescribeSlsLogStoreResponse:
        """
        @summary Queries information about a Logstore, such as the total capacity, storage duration, and used capacity.
        
        @param request: DescribeSlsLogStoreRequest
        @return: DescribeSlsLogStoreResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_sls_log_store_with_options(request, runtime)

    async def describe_sls_log_store_async(
        self,
        request: waf_openapi_20211001_models.DescribeSlsLogStoreRequest,
    ) -> waf_openapi_20211001_models.DescribeSlsLogStoreResponse:
        """
        @summary Queries information about a Logstore, such as the total capacity, storage duration, and used capacity.
        
        @param request: DescribeSlsLogStoreRequest
        @return: DescribeSlsLogStoreResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_sls_log_store_with_options_async(request, runtime)

    def describe_sls_log_store_status_with_options(
        self,
        request: waf_openapi_20211001_models.DescribeSlsLogStoreStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeSlsLogStoreStatusResponse:
        """
        @summary Queries the status of a Simple Log Service Logstore.
        
        @param request: DescribeSlsLogStoreStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSlsLogStoreStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSlsLogStoreStatus',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeSlsLogStoreStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sls_log_store_status_with_options_async(
        self,
        request: waf_openapi_20211001_models.DescribeSlsLogStoreStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeSlsLogStoreStatusResponse:
        """
        @summary Queries the status of a Simple Log Service Logstore.
        
        @param request: DescribeSlsLogStoreStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSlsLogStoreStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSlsLogStoreStatus',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeSlsLogStoreStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_sls_log_store_status(
        self,
        request: waf_openapi_20211001_models.DescribeSlsLogStoreStatusRequest,
    ) -> waf_openapi_20211001_models.DescribeSlsLogStoreStatusResponse:
        """
        @summary Queries the status of a Simple Log Service Logstore.
        
        @param request: DescribeSlsLogStoreStatusRequest
        @return: DescribeSlsLogStoreStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_sls_log_store_status_with_options(request, runtime)

    async def describe_sls_log_store_status_async(
        self,
        request: waf_openapi_20211001_models.DescribeSlsLogStoreStatusRequest,
    ) -> waf_openapi_20211001_models.DescribeSlsLogStoreStatusResponse:
        """
        @summary Queries the status of a Simple Log Service Logstore.
        
        @param request: DescribeSlsLogStoreStatusRequest
        @return: DescribeSlsLogStoreStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_sls_log_store_status_with_options_async(request, runtime)

    def describe_template_resource_count_with_options(
        self,
        request: waf_openapi_20211001_models.DescribeTemplateResourceCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeTemplateResourceCountResponse:
        """
        @summary Queries the number of protected resources for which a protection template takes effect.
        
        @param request: DescribeTemplateResourceCountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeTemplateResourceCountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.template_ids):
            query['TemplateIds'] = request.template_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTemplateResourceCount',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeTemplateResourceCountResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_template_resource_count_with_options_async(
        self,
        request: waf_openapi_20211001_models.DescribeTemplateResourceCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeTemplateResourceCountResponse:
        """
        @summary Queries the number of protected resources for which a protection template takes effect.
        
        @param request: DescribeTemplateResourceCountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeTemplateResourceCountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.template_ids):
            query['TemplateIds'] = request.template_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTemplateResourceCount',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeTemplateResourceCountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_template_resource_count(
        self,
        request: waf_openapi_20211001_models.DescribeTemplateResourceCountRequest,
    ) -> waf_openapi_20211001_models.DescribeTemplateResourceCountResponse:
        """
        @summary Queries the number of protected resources for which a protection template takes effect.
        
        @param request: DescribeTemplateResourceCountRequest
        @return: DescribeTemplateResourceCountResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_template_resource_count_with_options(request, runtime)

    async def describe_template_resource_count_async(
        self,
        request: waf_openapi_20211001_models.DescribeTemplateResourceCountRequest,
    ) -> waf_openapi_20211001_models.DescribeTemplateResourceCountResponse:
        """
        @summary Queries the number of protected resources for which a protection template takes effect.
        
        @param request: DescribeTemplateResourceCountRequest
        @return: DescribeTemplateResourceCountResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_template_resource_count_with_options_async(request, runtime)

    def describe_template_resources_with_options(
        self,
        request: waf_openapi_20211001_models.DescribeTemplateResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeTemplateResourcesResponse:
        """
        @summary Queries the resources that are associated to a protection rule template.
        
        @param request: DescribeTemplateResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeTemplateResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTemplateResources',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeTemplateResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_template_resources_with_options_async(
        self,
        request: waf_openapi_20211001_models.DescribeTemplateResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeTemplateResourcesResponse:
        """
        @summary Queries the resources that are associated to a protection rule template.
        
        @param request: DescribeTemplateResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeTemplateResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTemplateResources',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeTemplateResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_template_resources(
        self,
        request: waf_openapi_20211001_models.DescribeTemplateResourcesRequest,
    ) -> waf_openapi_20211001_models.DescribeTemplateResourcesResponse:
        """
        @summary Queries the resources that are associated to a protection rule template.
        
        @param request: DescribeTemplateResourcesRequest
        @return: DescribeTemplateResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_template_resources_with_options(request, runtime)

    async def describe_template_resources_async(
        self,
        request: waf_openapi_20211001_models.DescribeTemplateResourcesRequest,
    ) -> waf_openapi_20211001_models.DescribeTemplateResourcesResponse:
        """
        @summary Queries the resources that are associated to a protection rule template.
        
        @param request: DescribeTemplateResourcesRequest
        @return: DescribeTemplateResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_template_resources_with_options_async(request, runtime)

    def describe_user_sls_log_regions_with_options(
        self,
        request: waf_openapi_20211001_models.DescribeUserSlsLogRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeUserSlsLogRegionsResponse:
        """
        @summary Queries available regions for log storage.
        
        @param request: DescribeUserSlsLogRegionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeUserSlsLogRegionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUserSlsLogRegions',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeUserSlsLogRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_user_sls_log_regions_with_options_async(
        self,
        request: waf_openapi_20211001_models.DescribeUserSlsLogRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeUserSlsLogRegionsResponse:
        """
        @summary Queries available regions for log storage.
        
        @param request: DescribeUserSlsLogRegionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeUserSlsLogRegionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUserSlsLogRegions',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeUserSlsLogRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_user_sls_log_regions(
        self,
        request: waf_openapi_20211001_models.DescribeUserSlsLogRegionsRequest,
    ) -> waf_openapi_20211001_models.DescribeUserSlsLogRegionsResponse:
        """
        @summary Queries available regions for log storage.
        
        @param request: DescribeUserSlsLogRegionsRequest
        @return: DescribeUserSlsLogRegionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_user_sls_log_regions_with_options(request, runtime)

    async def describe_user_sls_log_regions_async(
        self,
        request: waf_openapi_20211001_models.DescribeUserSlsLogRegionsRequest,
    ) -> waf_openapi_20211001_models.DescribeUserSlsLogRegionsResponse:
        """
        @summary Queries available regions for log storage.
        
        @param request: DescribeUserSlsLogRegionsRequest
        @return: DescribeUserSlsLogRegionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_user_sls_log_regions_with_options_async(request, runtime)

    def describe_user_waf_log_status_with_options(
        self,
        request: waf_openapi_20211001_models.DescribeUserWafLogStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeUserWafLogStatusResponse:
        """
        @summary Queries the status, region ID, and status modification time of Web Application Firewall (WAF) logs.
        
        @param request: DescribeUserWafLogStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeUserWafLogStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUserWafLogStatus',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeUserWafLogStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_user_waf_log_status_with_options_async(
        self,
        request: waf_openapi_20211001_models.DescribeUserWafLogStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeUserWafLogStatusResponse:
        """
        @summary Queries the status, region ID, and status modification time of Web Application Firewall (WAF) logs.
        
        @param request: DescribeUserWafLogStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeUserWafLogStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUserWafLogStatus',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeUserWafLogStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_user_waf_log_status(
        self,
        request: waf_openapi_20211001_models.DescribeUserWafLogStatusRequest,
    ) -> waf_openapi_20211001_models.DescribeUserWafLogStatusResponse:
        """
        @summary Queries the status, region ID, and status modification time of Web Application Firewall (WAF) logs.
        
        @param request: DescribeUserWafLogStatusRequest
        @return: DescribeUserWafLogStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_user_waf_log_status_with_options(request, runtime)

    async def describe_user_waf_log_status_async(
        self,
        request: waf_openapi_20211001_models.DescribeUserWafLogStatusRequest,
    ) -> waf_openapi_20211001_models.DescribeUserWafLogStatusResponse:
        """
        @summary Queries the status, region ID, and status modification time of Web Application Firewall (WAF) logs.
        
        @param request: DescribeUserWafLogStatusRequest
        @return: DescribeUserWafLogStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_user_waf_log_status_with_options_async(request, runtime)

    def describe_visit_top_ip_with_options(
        self,
        request: waf_openapi_20211001_models.DescribeVisitTopIpRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeVisitTopIpResponse:
        """
        @summary Queries the top 10 IP addresses from which requests are sent.
        
        @param request: DescribeVisitTopIpRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeVisitTopIpResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_timestamp):
            query['EndTimestamp'] = request.end_timestamp
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource):
            query['Resource'] = request.resource
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.start_timestamp):
            query['StartTimestamp'] = request.start_timestamp
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVisitTopIp',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeVisitTopIpResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_visit_top_ip_with_options_async(
        self,
        request: waf_openapi_20211001_models.DescribeVisitTopIpRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeVisitTopIpResponse:
        """
        @summary Queries the top 10 IP addresses from which requests are sent.
        
        @param request: DescribeVisitTopIpRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeVisitTopIpResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_timestamp):
            query['EndTimestamp'] = request.end_timestamp
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource):
            query['Resource'] = request.resource
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.start_timestamp):
            query['StartTimestamp'] = request.start_timestamp
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVisitTopIp',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeVisitTopIpResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_visit_top_ip(
        self,
        request: waf_openapi_20211001_models.DescribeVisitTopIpRequest,
    ) -> waf_openapi_20211001_models.DescribeVisitTopIpResponse:
        """
        @summary Queries the top 10 IP addresses from which requests are sent.
        
        @param request: DescribeVisitTopIpRequest
        @return: DescribeVisitTopIpResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_visit_top_ip_with_options(request, runtime)

    async def describe_visit_top_ip_async(
        self,
        request: waf_openapi_20211001_models.DescribeVisitTopIpRequest,
    ) -> waf_openapi_20211001_models.DescribeVisitTopIpResponse:
        """
        @summary Queries the top 10 IP addresses from which requests are sent.
        
        @param request: DescribeVisitTopIpRequest
        @return: DescribeVisitTopIpResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_visit_top_ip_with_options_async(request, runtime)

    def describe_visit_uas_with_options(
        self,
        request: waf_openapi_20211001_models.DescribeVisitUasRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeVisitUasResponse:
        """
        @summary Queries the top 10 user agents that are used to initiate requests.
        
        @param request: DescribeVisitUasRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeVisitUasResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_timestamp):
            query['EndTimestamp'] = request.end_timestamp
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource):
            query['Resource'] = request.resource
        if not UtilClient.is_unset(request.start_timestamp):
            query['StartTimestamp'] = request.start_timestamp
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVisitUas',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeVisitUasResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_visit_uas_with_options_async(
        self,
        request: waf_openapi_20211001_models.DescribeVisitUasRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeVisitUasResponse:
        """
        @summary Queries the top 10 user agents that are used to initiate requests.
        
        @param request: DescribeVisitUasRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeVisitUasResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_timestamp):
            query['EndTimestamp'] = request.end_timestamp
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource):
            query['Resource'] = request.resource
        if not UtilClient.is_unset(request.start_timestamp):
            query['StartTimestamp'] = request.start_timestamp
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVisitUas',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeVisitUasResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_visit_uas(
        self,
        request: waf_openapi_20211001_models.DescribeVisitUasRequest,
    ) -> waf_openapi_20211001_models.DescribeVisitUasResponse:
        """
        @summary Queries the top 10 user agents that are used to initiate requests.
        
        @param request: DescribeVisitUasRequest
        @return: DescribeVisitUasResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_visit_uas_with_options(request, runtime)

    async def describe_visit_uas_async(
        self,
        request: waf_openapi_20211001_models.DescribeVisitUasRequest,
    ) -> waf_openapi_20211001_models.DescribeVisitUasResponse:
        """
        @summary Queries the top 10 user agents that are used to initiate requests.
        
        @param request: DescribeVisitUasRequest
        @return: DescribeVisitUasResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_visit_uas_with_options_async(request, runtime)

    def describe_waf_source_ip_segment_with_options(
        self,
        request: waf_openapi_20211001_models.DescribeWafSourceIpSegmentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeWafSourceIpSegmentResponse:
        """
        @summary Queries the back-to-origin CIDR blocks of a Web Application Firewall (WAF) instance.
        
        @param request: DescribeWafSourceIpSegmentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeWafSourceIpSegmentResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeWafSourceIpSegment',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeWafSourceIpSegmentResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_waf_source_ip_segment_with_options_async(
        self,
        request: waf_openapi_20211001_models.DescribeWafSourceIpSegmentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeWafSourceIpSegmentResponse:
        """
        @summary Queries the back-to-origin CIDR blocks of a Web Application Firewall (WAF) instance.
        
        @param request: DescribeWafSourceIpSegmentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeWafSourceIpSegmentResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeWafSourceIpSegment',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeWafSourceIpSegmentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_waf_source_ip_segment(
        self,
        request: waf_openapi_20211001_models.DescribeWafSourceIpSegmentRequest,
    ) -> waf_openapi_20211001_models.DescribeWafSourceIpSegmentResponse:
        """
        @summary Queries the back-to-origin CIDR blocks of a Web Application Firewall (WAF) instance.
        
        @param request: DescribeWafSourceIpSegmentRequest
        @return: DescribeWafSourceIpSegmentResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_waf_source_ip_segment_with_options(request, runtime)

    async def describe_waf_source_ip_segment_async(
        self,
        request: waf_openapi_20211001_models.DescribeWafSourceIpSegmentRequest,
    ) -> waf_openapi_20211001_models.DescribeWafSourceIpSegmentResponse:
        """
        @summary Queries the back-to-origin CIDR blocks of a Web Application Firewall (WAF) instance.
        
        @param request: DescribeWafSourceIpSegmentRequest
        @return: DescribeWafSourceIpSegmentResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_waf_source_ip_segment_with_options_async(request, runtime)

    def list_tag_keys_with_options(
        self,
        request: waf_openapi_20211001_models.ListTagKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.ListTagKeysResponse:
        """
        @summary Queries tag keys.
        
        @param request: ListTagKeysRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTagKeysResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagKeys',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.ListTagKeysResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tag_keys_with_options_async(
        self,
        request: waf_openapi_20211001_models.ListTagKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.ListTagKeysResponse:
        """
        @summary Queries tag keys.
        
        @param request: ListTagKeysRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTagKeysResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagKeys',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.ListTagKeysResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tag_keys(
        self,
        request: waf_openapi_20211001_models.ListTagKeysRequest,
    ) -> waf_openapi_20211001_models.ListTagKeysResponse:
        """
        @summary Queries tag keys.
        
        @param request: ListTagKeysRequest
        @return: ListTagKeysResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_tag_keys_with_options(request, runtime)

    async def list_tag_keys_async(
        self,
        request: waf_openapi_20211001_models.ListTagKeysRequest,
    ) -> waf_openapi_20211001_models.ListTagKeysResponse:
        """
        @summary Queries tag keys.
        
        @param request: ListTagKeysRequest
        @return: ListTagKeysResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_keys_with_options_async(request, runtime)

    def list_tag_resources_with_options(
        self,
        request: waf_openapi_20211001_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.ListTagResourcesResponse:
        """
        @summary Queries the tags that are added to a resource.
        
        @param request: ListTagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagResources',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.ListTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tag_resources_with_options_async(
        self,
        request: waf_openapi_20211001_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.ListTagResourcesResponse:
        """
        @summary Queries the tags that are added to a resource.
        
        @param request: ListTagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagResources',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.ListTagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tag_resources(
        self,
        request: waf_openapi_20211001_models.ListTagResourcesRequest,
    ) -> waf_openapi_20211001_models.ListTagResourcesResponse:
        """
        @summary Queries the tags that are added to a resource.
        
        @param request: ListTagResourcesRequest
        @return: ListTagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    async def list_tag_resources_async(
        self,
        request: waf_openapi_20211001_models.ListTagResourcesRequest,
    ) -> waf_openapi_20211001_models.ListTagResourcesResponse:
        """
        @summary Queries the tags that are added to a resource.
        
        @param request: ListTagResourcesRequest
        @return: ListTagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_resources_with_options_async(request, runtime)

    def list_tag_values_with_options(
        self,
        request: waf_openapi_20211001_models.ListTagValuesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.ListTagValuesResponse:
        """
        @summary Queries the tag values of a tag key.
        
        @param request: ListTagValuesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTagValuesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.key):
            query['Key'] = request.key
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagValues',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.ListTagValuesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tag_values_with_options_async(
        self,
        request: waf_openapi_20211001_models.ListTagValuesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.ListTagValuesResponse:
        """
        @summary Queries the tag values of a tag key.
        
        @param request: ListTagValuesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTagValuesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.key):
            query['Key'] = request.key
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagValues',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.ListTagValuesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tag_values(
        self,
        request: waf_openapi_20211001_models.ListTagValuesRequest,
    ) -> waf_openapi_20211001_models.ListTagValuesResponse:
        """
        @summary Queries the tag values of a tag key.
        
        @param request: ListTagValuesRequest
        @return: ListTagValuesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_tag_values_with_options(request, runtime)

    async def list_tag_values_async(
        self,
        request: waf_openapi_20211001_models.ListTagValuesRequest,
    ) -> waf_openapi_20211001_models.ListTagValuesResponse:
        """
        @summary Queries the tag values of a tag key.
        
        @param request: ListTagValuesRequest
        @return: ListTagValuesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_values_with_options_async(request, runtime)

    def modify_apisec_log_delivery_with_options(
        self,
        request: waf_openapi_20211001_models.ModifyApisecLogDeliveryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.ModifyApisecLogDeliveryResponse:
        """
        @summary 修改API安全日志订阅
        
        @param request: ModifyApisecLogDeliveryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyApisecLogDeliveryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.assert_key):
            query['AssertKey'] = request.assert_key
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.log_region_id):
            query['LogRegionId'] = request.log_region_id
        if not UtilClient.is_unset(request.log_store_name):
            query['LogStoreName'] = request.log_store_name
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyApisecLogDelivery',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.ModifyApisecLogDeliveryResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_apisec_log_delivery_with_options_async(
        self,
        request: waf_openapi_20211001_models.ModifyApisecLogDeliveryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.ModifyApisecLogDeliveryResponse:
        """
        @summary 修改API安全日志订阅
        
        @param request: ModifyApisecLogDeliveryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyApisecLogDeliveryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.assert_key):
            query['AssertKey'] = request.assert_key
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.log_region_id):
            query['LogRegionId'] = request.log_region_id
        if not UtilClient.is_unset(request.log_store_name):
            query['LogStoreName'] = request.log_store_name
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyApisecLogDelivery',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.ModifyApisecLogDeliveryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_apisec_log_delivery(
        self,
        request: waf_openapi_20211001_models.ModifyApisecLogDeliveryRequest,
    ) -> waf_openapi_20211001_models.ModifyApisecLogDeliveryResponse:
        """
        @summary 修改API安全日志订阅
        
        @param request: ModifyApisecLogDeliveryRequest
        @return: ModifyApisecLogDeliveryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_apisec_log_delivery_with_options(request, runtime)

    async def modify_apisec_log_delivery_async(
        self,
        request: waf_openapi_20211001_models.ModifyApisecLogDeliveryRequest,
    ) -> waf_openapi_20211001_models.ModifyApisecLogDeliveryResponse:
        """
        @summary 修改API安全日志订阅
        
        @param request: ModifyApisecLogDeliveryRequest
        @return: ModifyApisecLogDeliveryResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_apisec_log_delivery_with_options_async(request, runtime)

    def modify_apisec_log_delivery_status_with_options(
        self,
        request: waf_openapi_20211001_models.ModifyApisecLogDeliveryStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.ModifyApisecLogDeliveryStatusResponse:
        """
        @summary 修改API安全日志订阅状态
        
        @param request: ModifyApisecLogDeliveryStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyApisecLogDeliveryStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.assert_key):
            query['AssertKey'] = request.assert_key
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyApisecLogDeliveryStatus',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.ModifyApisecLogDeliveryStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_apisec_log_delivery_status_with_options_async(
        self,
        request: waf_openapi_20211001_models.ModifyApisecLogDeliveryStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.ModifyApisecLogDeliveryStatusResponse:
        """
        @summary 修改API安全日志订阅状态
        
        @param request: ModifyApisecLogDeliveryStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyApisecLogDeliveryStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.assert_key):
            query['AssertKey'] = request.assert_key
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyApisecLogDeliveryStatus',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.ModifyApisecLogDeliveryStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_apisec_log_delivery_status(
        self,
        request: waf_openapi_20211001_models.ModifyApisecLogDeliveryStatusRequest,
    ) -> waf_openapi_20211001_models.ModifyApisecLogDeliveryStatusResponse:
        """
        @summary 修改API安全日志订阅状态
        
        @param request: ModifyApisecLogDeliveryStatusRequest
        @return: ModifyApisecLogDeliveryStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_apisec_log_delivery_status_with_options(request, runtime)

    async def modify_apisec_log_delivery_status_async(
        self,
        request: waf_openapi_20211001_models.ModifyApisecLogDeliveryStatusRequest,
    ) -> waf_openapi_20211001_models.ModifyApisecLogDeliveryStatusResponse:
        """
        @summary 修改API安全日志订阅状态
        
        @param request: ModifyApisecLogDeliveryStatusRequest
        @return: ModifyApisecLogDeliveryStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_apisec_log_delivery_status_with_options_async(request, runtime)

    def modify_defense_resource_group_with_options(
        self,
        request: waf_openapi_20211001_models.ModifyDefenseResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.ModifyDefenseResourceGroupResponse:
        """
        @summary Modifies the configurations of a protected object group.
        
        @param request: ModifyDefenseResourceGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDefenseResourceGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.add_list):
            query['AddList'] = request.add_list
        if not UtilClient.is_unset(request.delete_list):
            query['DeleteList'] = request.delete_list
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDefenseResourceGroup',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.ModifyDefenseResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_defense_resource_group_with_options_async(
        self,
        request: waf_openapi_20211001_models.ModifyDefenseResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.ModifyDefenseResourceGroupResponse:
        """
        @summary Modifies the configurations of a protected object group.
        
        @param request: ModifyDefenseResourceGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDefenseResourceGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.add_list):
            query['AddList'] = request.add_list
        if not UtilClient.is_unset(request.delete_list):
            query['DeleteList'] = request.delete_list
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDefenseResourceGroup',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.ModifyDefenseResourceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_defense_resource_group(
        self,
        request: waf_openapi_20211001_models.ModifyDefenseResourceGroupRequest,
    ) -> waf_openapi_20211001_models.ModifyDefenseResourceGroupResponse:
        """
        @summary Modifies the configurations of a protected object group.
        
        @param request: ModifyDefenseResourceGroupRequest
        @return: ModifyDefenseResourceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_defense_resource_group_with_options(request, runtime)

    async def modify_defense_resource_group_async(
        self,
        request: waf_openapi_20211001_models.ModifyDefenseResourceGroupRequest,
    ) -> waf_openapi_20211001_models.ModifyDefenseResourceGroupResponse:
        """
        @summary Modifies the configurations of a protected object group.
        
        @param request: ModifyDefenseResourceGroupRequest
        @return: ModifyDefenseResourceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_defense_resource_group_with_options_async(request, runtime)

    def modify_defense_resource_xff_with_options(
        self,
        request: waf_openapi_20211001_models.ModifyDefenseResourceXffRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.ModifyDefenseResourceXffResponse:
        """
        @summary Modifies the cookie settings of a protected object and the method to identify the originating IP addresses of clients.
        
        @param request: ModifyDefenseResourceXffRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDefenseResourceXffResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acw_cookie_status):
            query['AcwCookieStatus'] = request.acw_cookie_status
        if not UtilClient.is_unset(request.acw_secure_status):
            query['AcwSecureStatus'] = request.acw_secure_status
        if not UtilClient.is_unset(request.acw_v3secure_status):
            query['AcwV3SecureStatus'] = request.acw_v3secure_status
        if not UtilClient.is_unset(request.custom_headers):
            query['CustomHeaders'] = request.custom_headers
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource):
            query['Resource'] = request.resource
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.xff_status):
            query['XffStatus'] = request.xff_status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDefenseResourceXff',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.ModifyDefenseResourceXffResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_defense_resource_xff_with_options_async(
        self,
        request: waf_openapi_20211001_models.ModifyDefenseResourceXffRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.ModifyDefenseResourceXffResponse:
        """
        @summary Modifies the cookie settings of a protected object and the method to identify the originating IP addresses of clients.
        
        @param request: ModifyDefenseResourceXffRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDefenseResourceXffResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acw_cookie_status):
            query['AcwCookieStatus'] = request.acw_cookie_status
        if not UtilClient.is_unset(request.acw_secure_status):
            query['AcwSecureStatus'] = request.acw_secure_status
        if not UtilClient.is_unset(request.acw_v3secure_status):
            query['AcwV3SecureStatus'] = request.acw_v3secure_status
        if not UtilClient.is_unset(request.custom_headers):
            query['CustomHeaders'] = request.custom_headers
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource):
            query['Resource'] = request.resource
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.xff_status):
            query['XffStatus'] = request.xff_status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDefenseResourceXff',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.ModifyDefenseResourceXffResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_defense_resource_xff(
        self,
        request: waf_openapi_20211001_models.ModifyDefenseResourceXffRequest,
    ) -> waf_openapi_20211001_models.ModifyDefenseResourceXffResponse:
        """
        @summary Modifies the cookie settings of a protected object and the method to identify the originating IP addresses of clients.
        
        @param request: ModifyDefenseResourceXffRequest
        @return: ModifyDefenseResourceXffResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_defense_resource_xff_with_options(request, runtime)

    async def modify_defense_resource_xff_async(
        self,
        request: waf_openapi_20211001_models.ModifyDefenseResourceXffRequest,
    ) -> waf_openapi_20211001_models.ModifyDefenseResourceXffResponse:
        """
        @summary Modifies the cookie settings of a protected object and the method to identify the originating IP addresses of clients.
        
        @param request: ModifyDefenseResourceXffRequest
        @return: ModifyDefenseResourceXffResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_defense_resource_xff_with_options_async(request, runtime)

    def modify_defense_rule_with_options(
        self,
        request: waf_openapi_20211001_models.ModifyDefenseRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.ModifyDefenseRuleResponse:
        """
        @summary Modifies the configurations of a protection rule.
        
        @param request: ModifyDefenseRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDefenseRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.defense_scene):
            query['DefenseScene'] = request.defense_scene
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.rules):
            query['Rules'] = request.rules
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDefenseRule',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.ModifyDefenseRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_defense_rule_with_options_async(
        self,
        request: waf_openapi_20211001_models.ModifyDefenseRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.ModifyDefenseRuleResponse:
        """
        @summary Modifies the configurations of a protection rule.
        
        @param request: ModifyDefenseRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDefenseRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.defense_scene):
            query['DefenseScene'] = request.defense_scene
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.rules):
            query['Rules'] = request.rules
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDefenseRule',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.ModifyDefenseRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_defense_rule(
        self,
        request: waf_openapi_20211001_models.ModifyDefenseRuleRequest,
    ) -> waf_openapi_20211001_models.ModifyDefenseRuleResponse:
        """
        @summary Modifies the configurations of a protection rule.
        
        @param request: ModifyDefenseRuleRequest
        @return: ModifyDefenseRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_defense_rule_with_options(request, runtime)

    async def modify_defense_rule_async(
        self,
        request: waf_openapi_20211001_models.ModifyDefenseRuleRequest,
    ) -> waf_openapi_20211001_models.ModifyDefenseRuleResponse:
        """
        @summary Modifies the configurations of a protection rule.
        
        @param request: ModifyDefenseRuleRequest
        @return: ModifyDefenseRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_defense_rule_with_options_async(request, runtime)

    def modify_defense_rule_cache_with_options(
        self,
        request: waf_openapi_20211001_models.ModifyDefenseRuleCacheRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.ModifyDefenseRuleCacheResponse:
        """
        @summary Updates the cached page of a website that is protected based on a website tamper-proofing rule.
        
        @param request: ModifyDefenseRuleCacheRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDefenseRuleCacheResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDefenseRuleCache',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.ModifyDefenseRuleCacheResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_defense_rule_cache_with_options_async(
        self,
        request: waf_openapi_20211001_models.ModifyDefenseRuleCacheRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.ModifyDefenseRuleCacheResponse:
        """
        @summary Updates the cached page of a website that is protected based on a website tamper-proofing rule.
        
        @param request: ModifyDefenseRuleCacheRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDefenseRuleCacheResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDefenseRuleCache',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.ModifyDefenseRuleCacheResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_defense_rule_cache(
        self,
        request: waf_openapi_20211001_models.ModifyDefenseRuleCacheRequest,
    ) -> waf_openapi_20211001_models.ModifyDefenseRuleCacheResponse:
        """
        @summary Updates the cached page of a website that is protected based on a website tamper-proofing rule.
        
        @param request: ModifyDefenseRuleCacheRequest
        @return: ModifyDefenseRuleCacheResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_defense_rule_cache_with_options(request, runtime)

    async def modify_defense_rule_cache_async(
        self,
        request: waf_openapi_20211001_models.ModifyDefenseRuleCacheRequest,
    ) -> waf_openapi_20211001_models.ModifyDefenseRuleCacheResponse:
        """
        @summary Updates the cached page of a website that is protected based on a website tamper-proofing rule.
        
        @param request: ModifyDefenseRuleCacheRequest
        @return: ModifyDefenseRuleCacheResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_defense_rule_cache_with_options_async(request, runtime)

    def modify_defense_rule_status_with_options(
        self,
        request: waf_openapi_20211001_models.ModifyDefenseRuleStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.ModifyDefenseRuleStatusResponse:
        """
        @summary Changes the status of a protection rule.
        
        @param request: ModifyDefenseRuleStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDefenseRuleStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        if not UtilClient.is_unset(request.rule_status):
            query['RuleStatus'] = request.rule_status
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDefenseRuleStatus',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.ModifyDefenseRuleStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_defense_rule_status_with_options_async(
        self,
        request: waf_openapi_20211001_models.ModifyDefenseRuleStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.ModifyDefenseRuleStatusResponse:
        """
        @summary Changes the status of a protection rule.
        
        @param request: ModifyDefenseRuleStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDefenseRuleStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        if not UtilClient.is_unset(request.rule_status):
            query['RuleStatus'] = request.rule_status
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDefenseRuleStatus',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.ModifyDefenseRuleStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_defense_rule_status(
        self,
        request: waf_openapi_20211001_models.ModifyDefenseRuleStatusRequest,
    ) -> waf_openapi_20211001_models.ModifyDefenseRuleStatusResponse:
        """
        @summary Changes the status of a protection rule.
        
        @param request: ModifyDefenseRuleStatusRequest
        @return: ModifyDefenseRuleStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_defense_rule_status_with_options(request, runtime)

    async def modify_defense_rule_status_async(
        self,
        request: waf_openapi_20211001_models.ModifyDefenseRuleStatusRequest,
    ) -> waf_openapi_20211001_models.ModifyDefenseRuleStatusResponse:
        """
        @summary Changes the status of a protection rule.
        
        @param request: ModifyDefenseRuleStatusRequest
        @return: ModifyDefenseRuleStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_defense_rule_status_with_options_async(request, runtime)

    def modify_defense_template_with_options(
        self,
        request: waf_openapi_20211001_models.ModifyDefenseTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.ModifyDefenseTemplateResponse:
        """
        @summary Modifies the configurations of a protection rule template.
        
        @param request: ModifyDefenseTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDefenseTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDefenseTemplate',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.ModifyDefenseTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_defense_template_with_options_async(
        self,
        request: waf_openapi_20211001_models.ModifyDefenseTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.ModifyDefenseTemplateResponse:
        """
        @summary Modifies the configurations of a protection rule template.
        
        @param request: ModifyDefenseTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDefenseTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDefenseTemplate',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.ModifyDefenseTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_defense_template(
        self,
        request: waf_openapi_20211001_models.ModifyDefenseTemplateRequest,
    ) -> waf_openapi_20211001_models.ModifyDefenseTemplateResponse:
        """
        @summary Modifies the configurations of a protection rule template.
        
        @param request: ModifyDefenseTemplateRequest
        @return: ModifyDefenseTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_defense_template_with_options(request, runtime)

    async def modify_defense_template_async(
        self,
        request: waf_openapi_20211001_models.ModifyDefenseTemplateRequest,
    ) -> waf_openapi_20211001_models.ModifyDefenseTemplateResponse:
        """
        @summary Modifies the configurations of a protection rule template.
        
        @param request: ModifyDefenseTemplateRequest
        @return: ModifyDefenseTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_defense_template_with_options_async(request, runtime)

    def modify_defense_template_status_with_options(
        self,
        request: waf_openapi_20211001_models.ModifyDefenseTemplateStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.ModifyDefenseTemplateStatusResponse:
        """
        @summary Changes the status of a protection rule template.
        
        @param request: ModifyDefenseTemplateStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDefenseTemplateStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.template_status):
            query['TemplateStatus'] = request.template_status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDefenseTemplateStatus',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.ModifyDefenseTemplateStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_defense_template_status_with_options_async(
        self,
        request: waf_openapi_20211001_models.ModifyDefenseTemplateStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.ModifyDefenseTemplateStatusResponse:
        """
        @summary Changes the status of a protection rule template.
        
        @param request: ModifyDefenseTemplateStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDefenseTemplateStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.template_status):
            query['TemplateStatus'] = request.template_status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDefenseTemplateStatus',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.ModifyDefenseTemplateStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_defense_template_status(
        self,
        request: waf_openapi_20211001_models.ModifyDefenseTemplateStatusRequest,
    ) -> waf_openapi_20211001_models.ModifyDefenseTemplateStatusResponse:
        """
        @summary Changes the status of a protection rule template.
        
        @param request: ModifyDefenseTemplateStatusRequest
        @return: ModifyDefenseTemplateStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_defense_template_status_with_options(request, runtime)

    async def modify_defense_template_status_async(
        self,
        request: waf_openapi_20211001_models.ModifyDefenseTemplateStatusRequest,
    ) -> waf_openapi_20211001_models.ModifyDefenseTemplateStatusResponse:
        """
        @summary Changes the status of a protection rule template.
        
        @param request: ModifyDefenseTemplateStatusRequest
        @return: ModifyDefenseTemplateStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_defense_template_status_with_options_async(request, runtime)

    def modify_domain_with_options(
        self,
        tmp_req: waf_openapi_20211001_models.ModifyDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.ModifyDomainResponse:
        """
        @summary Modifies the configurations of a domain name that is added to Web Application Firewall (WAF) in CNAME record mode.
        
        @param tmp_req: ModifyDomainRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDomainResponse
        """
        UtilClient.validate_model(tmp_req)
        request = waf_openapi_20211001_models.ModifyDomainShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.listen):
            request.listen_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.listen, 'Listen', 'json')
        if not UtilClient.is_unset(tmp_req.redirect):
            request.redirect_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.redirect, 'Redirect', 'json')
        query = {}
        if not UtilClient.is_unset(request.access_type):
            query['AccessType'] = request.access_type
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.listen_shrink):
            query['Listen'] = request.listen_shrink
        if not UtilClient.is_unset(request.redirect_shrink):
            query['Redirect'] = request.redirect_shrink
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDomain',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.ModifyDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_domain_with_options_async(
        self,
        tmp_req: waf_openapi_20211001_models.ModifyDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.ModifyDomainResponse:
        """
        @summary Modifies the configurations of a domain name that is added to Web Application Firewall (WAF) in CNAME record mode.
        
        @param tmp_req: ModifyDomainRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDomainResponse
        """
        UtilClient.validate_model(tmp_req)
        request = waf_openapi_20211001_models.ModifyDomainShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.listen):
            request.listen_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.listen, 'Listen', 'json')
        if not UtilClient.is_unset(tmp_req.redirect):
            request.redirect_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.redirect, 'Redirect', 'json')
        query = {}
        if not UtilClient.is_unset(request.access_type):
            query['AccessType'] = request.access_type
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.listen_shrink):
            query['Listen'] = request.listen_shrink
        if not UtilClient.is_unset(request.redirect_shrink):
            query['Redirect'] = request.redirect_shrink
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDomain',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.ModifyDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_domain(
        self,
        request: waf_openapi_20211001_models.ModifyDomainRequest,
    ) -> waf_openapi_20211001_models.ModifyDomainResponse:
        """
        @summary Modifies the configurations of a domain name that is added to Web Application Firewall (WAF) in CNAME record mode.
        
        @param request: ModifyDomainRequest
        @return: ModifyDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_domain_with_options(request, runtime)

    async def modify_domain_async(
        self,
        request: waf_openapi_20211001_models.ModifyDomainRequest,
    ) -> waf_openapi_20211001_models.ModifyDomainResponse:
        """
        @summary Modifies the configurations of a domain name that is added to Web Application Firewall (WAF) in CNAME record mode.
        
        @param request: ModifyDomainRequest
        @return: ModifyDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_domain_with_options_async(request, runtime)

    def modify_domain_punish_status_with_options(
        self,
        request: waf_openapi_20211001_models.ModifyDomainPunishStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.ModifyDomainPunishStatusResponse:
        """
        @summary Re-adds a domain name that is penalized for failing to obtain an Internet Content Provider (ICP) filing to Web Application Firewall (WAF).
        
        @param request: ModifyDomainPunishStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDomainPunishStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDomainPunishStatus',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.ModifyDomainPunishStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_domain_punish_status_with_options_async(
        self,
        request: waf_openapi_20211001_models.ModifyDomainPunishStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.ModifyDomainPunishStatusResponse:
        """
        @summary Re-adds a domain name that is penalized for failing to obtain an Internet Content Provider (ICP) filing to Web Application Firewall (WAF).
        
        @param request: ModifyDomainPunishStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDomainPunishStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDomainPunishStatus',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.ModifyDomainPunishStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_domain_punish_status(
        self,
        request: waf_openapi_20211001_models.ModifyDomainPunishStatusRequest,
    ) -> waf_openapi_20211001_models.ModifyDomainPunishStatusResponse:
        """
        @summary Re-adds a domain name that is penalized for failing to obtain an Internet Content Provider (ICP) filing to Web Application Firewall (WAF).
        
        @param request: ModifyDomainPunishStatusRequest
        @return: ModifyDomainPunishStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_domain_punish_status_with_options(request, runtime)

    async def modify_domain_punish_status_async(
        self,
        request: waf_openapi_20211001_models.ModifyDomainPunishStatusRequest,
    ) -> waf_openapi_20211001_models.ModifyDomainPunishStatusResponse:
        """
        @summary Re-adds a domain name that is penalized for failing to obtain an Internet Content Provider (ICP) filing to Web Application Firewall (WAF).
        
        @param request: ModifyDomainPunishStatusRequest
        @return: ModifyDomainPunishStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_domain_punish_status_with_options_async(request, runtime)

    def modify_hybrid_cloud_cluster_bypass_status_with_options(
        self,
        request: waf_openapi_20211001_models.ModifyHybridCloudClusterBypassStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.ModifyHybridCloudClusterBypassStatusResponse:
        """
        @summary Enables or disables manual bypass for a hybrid cloud cluster of the SDK-based traffic mirroring mode.
        
        @param request: ModifyHybridCloudClusterBypassStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyHybridCloudClusterBypassStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_resource_id):
            query['ClusterResourceId'] = request.cluster_resource_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.rule_status):
            query['RuleStatus'] = request.rule_status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyHybridCloudClusterBypassStatus',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.ModifyHybridCloudClusterBypassStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_hybrid_cloud_cluster_bypass_status_with_options_async(
        self,
        request: waf_openapi_20211001_models.ModifyHybridCloudClusterBypassStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.ModifyHybridCloudClusterBypassStatusResponse:
        """
        @summary Enables or disables manual bypass for a hybrid cloud cluster of the SDK-based traffic mirroring mode.
        
        @param request: ModifyHybridCloudClusterBypassStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyHybridCloudClusterBypassStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_resource_id):
            query['ClusterResourceId'] = request.cluster_resource_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.rule_status):
            query['RuleStatus'] = request.rule_status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyHybridCloudClusterBypassStatus',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.ModifyHybridCloudClusterBypassStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_hybrid_cloud_cluster_bypass_status(
        self,
        request: waf_openapi_20211001_models.ModifyHybridCloudClusterBypassStatusRequest,
    ) -> waf_openapi_20211001_models.ModifyHybridCloudClusterBypassStatusResponse:
        """
        @summary Enables or disables manual bypass for a hybrid cloud cluster of the SDK-based traffic mirroring mode.
        
        @param request: ModifyHybridCloudClusterBypassStatusRequest
        @return: ModifyHybridCloudClusterBypassStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_hybrid_cloud_cluster_bypass_status_with_options(request, runtime)

    async def modify_hybrid_cloud_cluster_bypass_status_async(
        self,
        request: waf_openapi_20211001_models.ModifyHybridCloudClusterBypassStatusRequest,
    ) -> waf_openapi_20211001_models.ModifyHybridCloudClusterBypassStatusResponse:
        """
        @summary Enables or disables manual bypass for a hybrid cloud cluster of the SDK-based traffic mirroring mode.
        
        @param request: ModifyHybridCloudClusterBypassStatusRequest
        @return: ModifyHybridCloudClusterBypassStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_hybrid_cloud_cluster_bypass_status_with_options_async(request, runtime)

    def modify_major_protection_black_ip_with_options(
        self,
        request: waf_openapi_20211001_models.ModifyMajorProtectionBlackIpRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.ModifyMajorProtectionBlackIpResponse:
        """
        @summary Modifies an IP address blacklist for major event protection.
        
        @param request: ModifyMajorProtectionBlackIpRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyMajorProtectionBlackIpResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.expired_time):
            query['ExpiredTime'] = request.expired_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.ip_list):
            query['IpList'] = request.ip_list
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyMajorProtectionBlackIp',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.ModifyMajorProtectionBlackIpResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_major_protection_black_ip_with_options_async(
        self,
        request: waf_openapi_20211001_models.ModifyMajorProtectionBlackIpRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.ModifyMajorProtectionBlackIpResponse:
        """
        @summary Modifies an IP address blacklist for major event protection.
        
        @param request: ModifyMajorProtectionBlackIpRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyMajorProtectionBlackIpResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.expired_time):
            query['ExpiredTime'] = request.expired_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.ip_list):
            query['IpList'] = request.ip_list
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyMajorProtectionBlackIp',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.ModifyMajorProtectionBlackIpResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_major_protection_black_ip(
        self,
        request: waf_openapi_20211001_models.ModifyMajorProtectionBlackIpRequest,
    ) -> waf_openapi_20211001_models.ModifyMajorProtectionBlackIpResponse:
        """
        @summary Modifies an IP address blacklist for major event protection.
        
        @param request: ModifyMajorProtectionBlackIpRequest
        @return: ModifyMajorProtectionBlackIpResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_major_protection_black_ip_with_options(request, runtime)

    async def modify_major_protection_black_ip_async(
        self,
        request: waf_openapi_20211001_models.ModifyMajorProtectionBlackIpRequest,
    ) -> waf_openapi_20211001_models.ModifyMajorProtectionBlackIpResponse:
        """
        @summary Modifies an IP address blacklist for major event protection.
        
        @param request: ModifyMajorProtectionBlackIpRequest
        @return: ModifyMajorProtectionBlackIpResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_major_protection_black_ip_with_options_async(request, runtime)

    def modify_member_account_with_options(
        self,
        request: waf_openapi_20211001_models.ModifyMemberAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.ModifyMemberAccountResponse:
        """
        @summary Modifies the information about members that are added for multi-account management.
        
        @param request: ModifyMemberAccountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyMemberAccountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.member_account_id):
            query['MemberAccountId'] = request.member_account_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyMemberAccount',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.ModifyMemberAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_member_account_with_options_async(
        self,
        request: waf_openapi_20211001_models.ModifyMemberAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.ModifyMemberAccountResponse:
        """
        @summary Modifies the information about members that are added for multi-account management.
        
        @param request: ModifyMemberAccountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyMemberAccountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.member_account_id):
            query['MemberAccountId'] = request.member_account_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyMemberAccount',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.ModifyMemberAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_member_account(
        self,
        request: waf_openapi_20211001_models.ModifyMemberAccountRequest,
    ) -> waf_openapi_20211001_models.ModifyMemberAccountResponse:
        """
        @summary Modifies the information about members that are added for multi-account management.
        
        @param request: ModifyMemberAccountRequest
        @return: ModifyMemberAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_member_account_with_options(request, runtime)

    async def modify_member_account_async(
        self,
        request: waf_openapi_20211001_models.ModifyMemberAccountRequest,
    ) -> waf_openapi_20211001_models.ModifyMemberAccountResponse:
        """
        @summary Modifies the information about members that are added for multi-account management.
        
        @param request: ModifyMemberAccountRequest
        @return: ModifyMemberAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_member_account_with_options_async(request, runtime)

    def modify_resource_log_status_with_options(
        self,
        request: waf_openapi_20211001_models.ModifyResourceLogStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.ModifyResourceLogStatusResponse:
        """
        @summary Enables or disables the log collection feature for a protected object.
        
        @param request: ModifyResourceLogStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyResourceLogStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource):
            query['Resource'] = request.resource
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyResourceLogStatus',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.ModifyResourceLogStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_resource_log_status_with_options_async(
        self,
        request: waf_openapi_20211001_models.ModifyResourceLogStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.ModifyResourceLogStatusResponse:
        """
        @summary Enables or disables the log collection feature for a protected object.
        
        @param request: ModifyResourceLogStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyResourceLogStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource):
            query['Resource'] = request.resource
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyResourceLogStatus',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.ModifyResourceLogStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_resource_log_status(
        self,
        request: waf_openapi_20211001_models.ModifyResourceLogStatusRequest,
    ) -> waf_openapi_20211001_models.ModifyResourceLogStatusResponse:
        """
        @summary Enables or disables the log collection feature for a protected object.
        
        @param request: ModifyResourceLogStatusRequest
        @return: ModifyResourceLogStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_resource_log_status_with_options(request, runtime)

    async def modify_resource_log_status_async(
        self,
        request: waf_openapi_20211001_models.ModifyResourceLogStatusRequest,
    ) -> waf_openapi_20211001_models.ModifyResourceLogStatusResponse:
        """
        @summary Enables or disables the log collection feature for a protected object.
        
        @param request: ModifyResourceLogStatusRequest
        @return: ModifyResourceLogStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_resource_log_status_with_options_async(request, runtime)

    def modify_template_resources_with_options(
        self,
        request: waf_openapi_20211001_models.ModifyTemplateResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.ModifyTemplateResourcesResponse:
        """
        @summary Associates or disassociates a protected object or protected object group with or from a protection rule template.
        
        @param request: ModifyTemplateResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyTemplateResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bind_resource_groups):
            query['BindResourceGroups'] = request.bind_resource_groups
        if not UtilClient.is_unset(request.bind_resources):
            query['BindResources'] = request.bind_resources
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.unbind_resource_groups):
            query['UnbindResourceGroups'] = request.unbind_resource_groups
        if not UtilClient.is_unset(request.unbind_resources):
            query['UnbindResources'] = request.unbind_resources
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyTemplateResources',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.ModifyTemplateResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_template_resources_with_options_async(
        self,
        request: waf_openapi_20211001_models.ModifyTemplateResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.ModifyTemplateResourcesResponse:
        """
        @summary Associates or disassociates a protected object or protected object group with or from a protection rule template.
        
        @param request: ModifyTemplateResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyTemplateResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bind_resource_groups):
            query['BindResourceGroups'] = request.bind_resource_groups
        if not UtilClient.is_unset(request.bind_resources):
            query['BindResources'] = request.bind_resources
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.unbind_resource_groups):
            query['UnbindResourceGroups'] = request.unbind_resource_groups
        if not UtilClient.is_unset(request.unbind_resources):
            query['UnbindResources'] = request.unbind_resources
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyTemplateResources',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.ModifyTemplateResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_template_resources(
        self,
        request: waf_openapi_20211001_models.ModifyTemplateResourcesRequest,
    ) -> waf_openapi_20211001_models.ModifyTemplateResourcesResponse:
        """
        @summary Associates or disassociates a protected object or protected object group with or from a protection rule template.
        
        @param request: ModifyTemplateResourcesRequest
        @return: ModifyTemplateResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_template_resources_with_options(request, runtime)

    async def modify_template_resources_async(
        self,
        request: waf_openapi_20211001_models.ModifyTemplateResourcesRequest,
    ) -> waf_openapi_20211001_models.ModifyTemplateResourcesResponse:
        """
        @summary Associates or disassociates a protected object or protected object group with or from a protection rule template.
        
        @param request: ModifyTemplateResourcesRequest
        @return: ModifyTemplateResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_template_resources_with_options_async(request, runtime)

    def sync_product_instance_with_options(
        self,
        request: waf_openapi_20211001_models.SyncProductInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.SyncProductInstanceResponse:
        """
        @summary Synchronizes Elastic Compute Service (ECS) instances and Classic Load Balancer (CLB) instances to Web Application Firewall (WAF).
        
        @description SyncProductInstance is an asynchronous operation. You can call the [DescribeProductInstances](https://help.aliyun.com/document_detail/2743168.html) operation to query the status of the task.
        
        @param request: SyncProductInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SyncProductInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SyncProductInstance',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.SyncProductInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def sync_product_instance_with_options_async(
        self,
        request: waf_openapi_20211001_models.SyncProductInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.SyncProductInstanceResponse:
        """
        @summary Synchronizes Elastic Compute Service (ECS) instances and Classic Load Balancer (CLB) instances to Web Application Firewall (WAF).
        
        @description SyncProductInstance is an asynchronous operation. You can call the [DescribeProductInstances](https://help.aliyun.com/document_detail/2743168.html) operation to query the status of the task.
        
        @param request: SyncProductInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SyncProductInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SyncProductInstance',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.SyncProductInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def sync_product_instance(
        self,
        request: waf_openapi_20211001_models.SyncProductInstanceRequest,
    ) -> waf_openapi_20211001_models.SyncProductInstanceResponse:
        """
        @summary Synchronizes Elastic Compute Service (ECS) instances and Classic Load Balancer (CLB) instances to Web Application Firewall (WAF).
        
        @description SyncProductInstance is an asynchronous operation. You can call the [DescribeProductInstances](https://help.aliyun.com/document_detail/2743168.html) operation to query the status of the task.
        
        @param request: SyncProductInstanceRequest
        @return: SyncProductInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.sync_product_instance_with_options(request, runtime)

    async def sync_product_instance_async(
        self,
        request: waf_openapi_20211001_models.SyncProductInstanceRequest,
    ) -> waf_openapi_20211001_models.SyncProductInstanceResponse:
        """
        @summary Synchronizes Elastic Compute Service (ECS) instances and Classic Load Balancer (CLB) instances to Web Application Firewall (WAF).
        
        @description SyncProductInstance is an asynchronous operation. You can call the [DescribeProductInstances](https://help.aliyun.com/document_detail/2743168.html) operation to query the status of the task.
        
        @param request: SyncProductInstanceRequest
        @return: SyncProductInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.sync_product_instance_with_options_async(request, runtime)

    def tag_resources_with_options(
        self,
        request: waf_openapi_20211001_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.TagResourcesResponse:
        """
        @summary Adds tags to resources.
        
        @param request: TagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TagResources',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.TagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def tag_resources_with_options_async(
        self,
        request: waf_openapi_20211001_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.TagResourcesResponse:
        """
        @summary Adds tags to resources.
        
        @param request: TagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TagResources',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.TagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def tag_resources(
        self,
        request: waf_openapi_20211001_models.TagResourcesRequest,
    ) -> waf_openapi_20211001_models.TagResourcesResponse:
        """
        @summary Adds tags to resources.
        
        @param request: TagResourcesRequest
        @return: TagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    async def tag_resources_async(
        self,
        request: waf_openapi_20211001_models.TagResourcesRequest,
    ) -> waf_openapi_20211001_models.TagResourcesResponse:
        """
        @summary Adds tags to resources.
        
        @param request: TagResourcesRequest
        @return: TagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.tag_resources_with_options_async(request, runtime)

    def untag_resources_with_options(
        self,
        request: waf_openapi_20211001_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.UntagResourcesResponse:
        """
        @summary Removes tags from resources and then deletes the tags.
        
        @param request: UntagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UntagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UntagResources',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.UntagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def untag_resources_with_options_async(
        self,
        request: waf_openapi_20211001_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.UntagResourcesResponse:
        """
        @summary Removes tags from resources and then deletes the tags.
        
        @param request: UntagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UntagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UntagResources',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.UntagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def untag_resources(
        self,
        request: waf_openapi_20211001_models.UntagResourcesRequest,
    ) -> waf_openapi_20211001_models.UntagResourcesResponse:
        """
        @summary Removes tags from resources and then deletes the tags.
        
        @param request: UntagResourcesRequest
        @return: UntagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)

    async def untag_resources_async(
        self,
        request: waf_openapi_20211001_models.UntagResourcesRequest,
    ) -> waf_openapi_20211001_models.UntagResourcesResponse:
        """
        @summary Removes tags from resources and then deletes the tags.
        
        @param request: UntagResourcesRequest
        @return: UntagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.untag_resources_with_options_async(request, runtime)
