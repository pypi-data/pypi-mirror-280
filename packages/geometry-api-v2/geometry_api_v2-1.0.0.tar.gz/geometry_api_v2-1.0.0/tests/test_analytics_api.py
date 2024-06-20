from shapediver.geometry_api_v2.client import (
    AnalyticsApi,
    AtLeastOneUuid,
    Configuration,
    ReqAnyCreditMetricId,
    ReqCreditMetric,
    ReqCreditMetrics,
    ReqModelCreditMetricId,
    ReqModelStatistic,
    ReqModelStatistics,
    SessionApi,
)
from shapediver.geometry_api_v2.sd_client import SdClient


def test_model_session_statistics(utils, host, jwt_model, model_id):
    model_client = SdClient(Configuration(host, access_token=jwt_model))

    # Initialize a new session.
    ticket = utils.create_ticket()
    session_id = SessionApi(model_client).create_session_by_ticket(ticket).session_id

    # Fetch model statistics within a specific time range.
    req_stats = ReqModelStatistics(
        parameters=[
            ReqModelStatistic(
                modelid=AtLeastOneUuid(model_id),
                timestamp_from="2024",
                timestamp_to="2025",
            )
        ]
    )
    res_stats = AnalyticsApi(model_client).get_model_statistics(req_stats)
    assert len(res_stats.analytics.models) > 0

    # Close the session.
    SessionApi(model_client).close_session(session_id)


def test_credit_metrics(utils, host, jwt_model, model_id):
    model_client = SdClient(Configuration(host, access_token=jwt_model))

    # Initialize a new session.
    ticket = utils.create_ticket()
    session_id = SessionApi(model_client).create_session_by_ticket(ticket).session_id

    # Fetch credit metrics within a specific time range.
    req_credits = ReqCreditMetrics(
        parameters=[
            ReqCreditMetric(
                id=ReqAnyCreditMetricId(
                    ReqModelCreditMetricId(modelIds=AtLeastOneUuid(model_id))
                ),
                timestamp_from="2024",
                timestamp_to="2025",
            )
        ]
    )
    res_credits = AnalyticsApi(model_client).get_credit_metrics(req_credits)
    assert len(res_credits.analytics.credit_metrics) > 0

    # Close the session.
    SessionApi(model_client).close_session(session_id)
