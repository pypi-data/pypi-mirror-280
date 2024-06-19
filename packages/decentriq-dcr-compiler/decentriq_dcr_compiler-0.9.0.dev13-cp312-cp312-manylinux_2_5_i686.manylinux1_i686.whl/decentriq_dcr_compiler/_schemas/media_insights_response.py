# generated by datamodel-codegen:
#   filename:  media_insights_response.json

from __future__ import annotations

from enum import Enum
from typing import Any, Mapping, Optional, Sequence, Union

from pydantic import BaseModel, ConfigDict, Field, RootModel, conint


class PublishDataRoom(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    dataRoomId: str


class MediaInsightsResponse1(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    publishDataRoom: PublishDataRoom


class MediaInsightsResponse3(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    publishAdvertiserDataset: Mapping[str, Any]


class MediaInsightsResponse4(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    publishPublisherUsersDataset: Mapping[str, Any]


class MediaInsightsResponse5(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    unpublishPublisherUsersDataset: Mapping[str, Any]


class MediaInsightsResponse6(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    publishDemographicsDataset: Mapping[str, Any]


class MediaInsightsResponse7(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    unpublishDemographicsDataset: Mapping[str, Any]


class MediaInsightsResponse8(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    publishSegmentsDataset: Mapping[str, Any]


class MediaInsightsResponse9(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    unpublishSegmentsDataset: Mapping[str, Any]


class MediaInsightsResponse10(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    publishEmbeddingsDataset: Mapping[str, Any]


class MediaInsightsResponse11(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    unpublishEmbeddingsDataset: Mapping[str, Any]


class MediaInsightsResponse12(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    unpublishAdvertiserDataset: Mapping[str, Any]


class RetrievePublishedDatasets(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    advertiserDatasetHashHex: Optional[str] = None
    demographicsDatasetHashHex: Optional[str] = None
    embeddingsDatasetHashHex: Optional[str] = None
    publisherDatasetHashHex: Optional[str] = None
    segmentsDatasetHashHex: Optional[str] = None


class MediaInsightsResponse13(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    retrievePublishedDatasets: RetrievePublishedDatasets


class ComputeAvailableAudiences(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    computeNodeName: str
    jobIdHex: str


class MediaInsightsResponse14(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    computeAvailableAudiences: ComputeAvailableAudiences


class ComputeOverlapStatistics(ComputeAvailableAudiences):
    pass


class MediaInsightsResponse15(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    computeOverlapStatistics: ComputeOverlapStatistics


class ComputeInsights(ComputeAvailableAudiences):
    pass


class MediaInsightsResponse16(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    computeInsights: ComputeInsights


class MediaInsightsResponse17(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    publishActivatedAudiencesConfig: Mapping[str, Any]


class MediaInsightsResponse18(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    unpublishActivatedAudiencesConfig: Mapping[str, Any]


class GetAudienceUserList(ComputeAvailableAudiences):
    pass


class MediaInsightsResponse19(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    getAudienceUserList: GetAudienceUserList


class GetAudienceUserListForAdvertiser(ComputeAvailableAudiences):
    pass


class MediaInsightsResponse20(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    getAudienceUserListForAdvertiser: GetAudienceUserListForAdvertiser


class GetAudiencesForPublisher(ComputeAvailableAudiences):
    pass


class MediaInsightsResponse21(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    getAudiencesForPublisher: GetAudiencesForPublisher


class GetAudiencesForAdvertiser(ComputeAvailableAudiences):
    pass


class MediaInsightsResponse22(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    getAudiencesForAdvertiser: GetAudiencesForAdvertiser


class IngestAudiencesReport(ComputeAvailableAudiences):
    pass


class MediaInsightsResponse23(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    ingestAudiencesReport: IngestAudiencesReport


class RetrieveModelQualityReport(ComputeAvailableAudiences):
    pass


class MediaInsightsResponse24(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    retrieveModelQualityReport: RetrieveModelQualityReport


class EnclaveSpecificationV0(BaseModel):
    attestationProtoBase64: str
    id: str
    workerProtocol: conint(ge=0)


class FormatType(Enum):
    STRING = 'STRING'
    INTEGER = 'INTEGER'
    FLOAT = 'FLOAT'
    EMAIL = 'EMAIL'
    DATE_ISO8601 = 'DATE_ISO8601'
    PHONE_NUMBER_E164 = 'PHONE_NUMBER_E164'
    HASH_SHA256_HEX = 'HASH_SHA256_HEX'


class HashingAlgorithm(Enum):
    SHA256_HEX = 'SHA256_HEX'


class ModelEvaluationType(Enum):
    ROC_CURVE = 'ROC_CURVE'
    DISTANCE_TO_EMBEDDING = 'DISTANCE_TO_EMBEDDING'
    JACCARD = 'JACCARD'


class Type(Enum):
    SUPPORTED = 'SUPPORTED'


class RequirementFlagValue19(BaseModel):
    type: Type


class Type19(Enum):
    DATASET = 'DATASET'


class RequirementFlagValue20(BaseModel):
    type: Type19


class Type20(Enum):
    PROPERTY = 'PROPERTY'


class RequirementFlagValue21(BaseModel):
    type: Type20
    value: str


class RequirementFlagValue(
    RootModel[
        Union[RequirementFlagValue19, RequirementFlagValue20, RequirementFlagValue21]
    ]
):
    root: Union[RequirementFlagValue19, RequirementFlagValue20, RequirementFlagValue21]


class KnownOrUnknownRequirementFlagValue(RootModel[Optional[RequirementFlagValue]]):
    root: Optional[RequirementFlagValue]


class ModelEvaluationConfig(BaseModel):
    postScopeMerge: Sequence[ModelEvaluationType]
    preScopeMerge: Sequence[ModelEvaluationType]


class RequirementFlag(BaseModel):
    details: KnownOrUnknownRequirementFlagValue
    name: str


class RequirementOp12(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    has: RequirementFlag


class MediaInsightsComputeV0(BaseModel):
    advertiserEmails: Sequence[str]
    agencyEmails: Sequence[str]
    authenticationRootCertificatePem: str
    driverEnclaveSpecification: EnclaveSpecificationV0
    hashMatchingIdWith: Optional[HashingAlgorithm] = None
    id: str
    mainAdvertiserEmail: str
    mainPublisherEmail: str
    matchingIdFormat: FormatType
    modelEvaluation: Optional[ModelEvaluationConfig] = None
    name: str
    observerEmails: Sequence[str]
    publisherEmails: Sequence[str]
    pythonEnclaveSpecification: EnclaveSpecificationV0
    rateLimitPublishDataNumPerWindow: Optional[conint(ge=0)] = 10
    rateLimitPublishDataWindowSeconds: Optional[conint(ge=0)] = 604800


class MediaInsightsComputeV1(MediaInsightsComputeV0):
    pass


class MediaInsightsComputeV2(BaseModel):
    advertiserEmails: Sequence[str]
    agencyEmails: Sequence[str]
    authenticationRootCertificatePem: str
    dataPartnerEmails: Optional[Sequence[str]] = None
    driverEnclaveSpecification: EnclaveSpecificationV0
    hashMatchingIdWith: Optional[HashingAlgorithm] = None
    id: str
    mainAdvertiserEmail: str
    mainPublisherEmail: str
    matchingIdFormat: FormatType
    modelEvaluation: Optional[ModelEvaluationConfig] = None
    name: str
    observerEmails: Sequence[str]
    publisherEmails: Sequence[str]
    pythonEnclaveSpecification: EnclaveSpecificationV0
    rateLimitPublishDataNumPerWindow: Optional[conint(ge=0)] = 10
    rateLimitPublishDataWindowSeconds: Optional[conint(ge=0)] = 604800


class MediaInsightsCompute(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    v0: MediaInsightsComputeV0


class MediaInsightsCompute10(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    v1: MediaInsightsComputeV1


class MediaInsightsCompute11(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    v2: MediaInsightsComputeV2


class MediaInsightsCompute8(
    RootModel[
        Union[MediaInsightsCompute, MediaInsightsCompute10, MediaInsightsCompute11]
    ]
):
    root: Union[MediaInsightsCompute, MediaInsightsCompute10, MediaInsightsCompute11]


class MediaInsightsComputeOrUnknown(RootModel[Optional[MediaInsightsCompute8]]):
    root: Optional[MediaInsightsCompute8]


class RetrieveDataRoom(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    dataRoom: MediaInsightsDcr


class MediaInsightsResponse2(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    retrieveDataRoom: RetrieveDataRoom


class MediaInsightsResponse(
    RootModel[
        Union[
            MediaInsightsResponse1,
            MediaInsightsResponse2,
            MediaInsightsResponse3,
            MediaInsightsResponse4,
            MediaInsightsResponse5,
            MediaInsightsResponse6,
            MediaInsightsResponse7,
            MediaInsightsResponse8,
            MediaInsightsResponse9,
            MediaInsightsResponse10,
            MediaInsightsResponse11,
            MediaInsightsResponse12,
            MediaInsightsResponse13,
            MediaInsightsResponse14,
            MediaInsightsResponse15,
            MediaInsightsResponse16,
            MediaInsightsResponse17,
            MediaInsightsResponse18,
            MediaInsightsResponse19,
            MediaInsightsResponse20,
            MediaInsightsResponse21,
            MediaInsightsResponse22,
            MediaInsightsResponse23,
            MediaInsightsResponse24,
        ]
    ]
):
    root: Union[
        MediaInsightsResponse1,
        MediaInsightsResponse2,
        MediaInsightsResponse3,
        MediaInsightsResponse4,
        MediaInsightsResponse5,
        MediaInsightsResponse6,
        MediaInsightsResponse7,
        MediaInsightsResponse8,
        MediaInsightsResponse9,
        MediaInsightsResponse10,
        MediaInsightsResponse11,
        MediaInsightsResponse12,
        MediaInsightsResponse13,
        MediaInsightsResponse14,
        MediaInsightsResponse15,
        MediaInsightsResponse16,
        MediaInsightsResponse17,
        MediaInsightsResponse18,
        MediaInsightsResponse19,
        MediaInsightsResponse20,
        MediaInsightsResponse21,
        MediaInsightsResponse22,
        MediaInsightsResponse23,
        MediaInsightsResponse24,
    ] = Field(..., title='MediaInsightsResponse')


class ConsumerRequirements(BaseModel):
    optional: Sequence[RequirementFlag]
    required: Optional[RequirementOp] = None


class MediaInsightsDcr3(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    v0: MediaInsightsDcrInner


class MediaInsightsDcr(RootModel[MediaInsightsDcr3]):
    root: MediaInsightsDcr3


class MediaInsightsDcrInner(BaseModel):
    compute: MediaInsightsComputeOrUnknown
    consumes: ConsumerRequirements
    features: Sequence[str]


class RequirementOp9(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    or_: Sequence[RequirementOp] = Field(..., alias='or')


class RequirementOp10(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    and_: Sequence[RequirementOp] = Field(..., alias='and')


class RequirementOp11(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    exclusiveOr: Sequence[RequirementOp]


class RequirementOp(
    RootModel[Union[RequirementOp9, RequirementOp10, RequirementOp11, RequirementOp12]]
):
    root: Union[
        RequirementOp9, RequirementOp10, RequirementOp11, RequirementOp12
    ] = Field(
        ...,
        description='An expression that can be used to check whether a data lab (as a "data provider") provides certain datasets or certain data properties. This was introduced because the system used in the LM DCR didn\'t allow the MediaInsights DCR to express that _either_ a segments or an embeddings dataset is required in case it was configured to enable lookalike modelling.',
    )


RetrieveDataRoom.model_rebuild()
ConsumerRequirements.model_rebuild()
MediaInsightsDcr3.model_rebuild()
RequirementOp9.model_rebuild()
RequirementOp10.model_rebuild()
RequirementOp11.model_rebuild()
