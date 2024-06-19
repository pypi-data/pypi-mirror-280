# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'GetDecryptedDataResult',
    'AwaitableGetDecryptedDataResult',
    'get_decrypted_data',
    'get_decrypted_data_output',
]

@pulumi.output_type
class GetDecryptedDataResult:
    """
    A collection of values returned by getDecryptedData.
    """
    def __init__(__self__, associated_data=None, ciphertext=None, crypto_endpoint=None, id=None, key_id=None, plaintext=None, plaintext_checksum=None):
        if associated_data and not isinstance(associated_data, dict):
            raise TypeError("Expected argument 'associated_data' to be a dict")
        pulumi.set(__self__, "associated_data", associated_data)
        if ciphertext and not isinstance(ciphertext, str):
            raise TypeError("Expected argument 'ciphertext' to be a str")
        pulumi.set(__self__, "ciphertext", ciphertext)
        if crypto_endpoint and not isinstance(crypto_endpoint, str):
            raise TypeError("Expected argument 'crypto_endpoint' to be a str")
        pulumi.set(__self__, "crypto_endpoint", crypto_endpoint)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if key_id and not isinstance(key_id, str):
            raise TypeError("Expected argument 'key_id' to be a str")
        pulumi.set(__self__, "key_id", key_id)
        if plaintext and not isinstance(plaintext, str):
            raise TypeError("Expected argument 'plaintext' to be a str")
        pulumi.set(__self__, "plaintext", plaintext)
        if plaintext_checksum and not isinstance(plaintext_checksum, str):
            raise TypeError("Expected argument 'plaintext_checksum' to be a str")
        pulumi.set(__self__, "plaintext_checksum", plaintext_checksum)

    @property
    @pulumi.getter(name="associatedData")
    def associated_data(self) -> Optional[Mapping[str, Any]]:
        return pulumi.get(self, "associated_data")

    @property
    @pulumi.getter
    def ciphertext(self) -> str:
        return pulumi.get(self, "ciphertext")

    @property
    @pulumi.getter(name="cryptoEndpoint")
    def crypto_endpoint(self) -> str:
        return pulumi.get(self, "crypto_endpoint")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="keyId")
    def key_id(self) -> str:
        return pulumi.get(self, "key_id")

    @property
    @pulumi.getter
    def plaintext(self) -> str:
        """
        The decrypted data, in the form of a base64-encoded value.
        """
        return pulumi.get(self, "plaintext")

    @property
    @pulumi.getter(name="plaintextChecksum")
    def plaintext_checksum(self) -> str:
        """
        Checksum of the decrypted data.
        """
        return pulumi.get(self, "plaintext_checksum")


class AwaitableGetDecryptedDataResult(GetDecryptedDataResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDecryptedDataResult(
            associated_data=self.associated_data,
            ciphertext=self.ciphertext,
            crypto_endpoint=self.crypto_endpoint,
            id=self.id,
            key_id=self.key_id,
            plaintext=self.plaintext,
            plaintext_checksum=self.plaintext_checksum)


def get_decrypted_data(associated_data: Optional[Mapping[str, Any]] = None,
                       ciphertext: Optional[str] = None,
                       crypto_endpoint: Optional[str] = None,
                       key_id: Optional[str] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDecryptedDataResult:
    """
    The `kms_get_decrypted_data` data source provides details about a specific DecryptedData

    Decrypts data using the given DecryptDataDetails resource.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_decrypted_data = oci.Kms.get_decrypted_data(ciphertext=decrypted_data_ciphertext,
        crypto_endpoint=decrypted_data_crypto_endpoint,
        key_id=test_key["id"],
        associated_data=decrypted_data_associated_data)
    ```


    :param Mapping[str, Any] associated_data: Information that can be used to provide an encryption context for the  encrypted data. The length of the string representation of the associatedData must be fewer than 4096 characters.
    :param str ciphertext: The encrypted data to decrypt.
    :param str crypto_endpoint: The service endpoint to perform cryptographic operations against. Cryptographic operations include 'Encrypt,' 'Decrypt,' and 'GenerateDataEncryptionKey' operations. see Vault Crypto endpoint.
    :param str key_id: The OCID of the key used to encrypt the ciphertext.
    """
    __args__ = dict()
    __args__['associatedData'] = associated_data
    __args__['ciphertext'] = ciphertext
    __args__['cryptoEndpoint'] = crypto_endpoint
    __args__['keyId'] = key_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:Kms/getDecryptedData:getDecryptedData', __args__, opts=opts, typ=GetDecryptedDataResult).value

    return AwaitableGetDecryptedDataResult(
        associated_data=pulumi.get(__ret__, 'associated_data'),
        ciphertext=pulumi.get(__ret__, 'ciphertext'),
        crypto_endpoint=pulumi.get(__ret__, 'crypto_endpoint'),
        id=pulumi.get(__ret__, 'id'),
        key_id=pulumi.get(__ret__, 'key_id'),
        plaintext=pulumi.get(__ret__, 'plaintext'),
        plaintext_checksum=pulumi.get(__ret__, 'plaintext_checksum'))


@_utilities.lift_output_func(get_decrypted_data)
def get_decrypted_data_output(associated_data: Optional[pulumi.Input[Optional[Mapping[str, Any]]]] = None,
                              ciphertext: Optional[pulumi.Input[str]] = None,
                              crypto_endpoint: Optional[pulumi.Input[str]] = None,
                              key_id: Optional[pulumi.Input[str]] = None,
                              opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetDecryptedDataResult]:
    """
    The `kms_get_decrypted_data` data source provides details about a specific DecryptedData

    Decrypts data using the given DecryptDataDetails resource.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_decrypted_data = oci.Kms.get_decrypted_data(ciphertext=decrypted_data_ciphertext,
        crypto_endpoint=decrypted_data_crypto_endpoint,
        key_id=test_key["id"],
        associated_data=decrypted_data_associated_data)
    ```


    :param Mapping[str, Any] associated_data: Information that can be used to provide an encryption context for the  encrypted data. The length of the string representation of the associatedData must be fewer than 4096 characters.
    :param str ciphertext: The encrypted data to decrypt.
    :param str crypto_endpoint: The service endpoint to perform cryptographic operations against. Cryptographic operations include 'Encrypt,' 'Decrypt,' and 'GenerateDataEncryptionKey' operations. see Vault Crypto endpoint.
    :param str key_id: The OCID of the key used to encrypt the ciphertext.
    """
    ...
