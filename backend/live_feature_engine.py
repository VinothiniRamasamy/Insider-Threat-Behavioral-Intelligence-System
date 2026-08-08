import pandas as pd
from user_activity import update_user


def create_live_features(log, baseline):

    # Update live user activity
    activity = update_user(log)

    feature = {}

    # Dynamic features
    feature["http_requests_deviation"] = (
        activity["http_requests"] -
        baseline["http_requests"]
    )

    feature["cloud_job_visits_deviation"] = (
        activity["cloud_job_visits"] -
        baseline["cloud_job_visits"]
    )

    # Keep remaining features from baseline (demo values)
    feature["logon_count_deviation"] = 0 - baseline["logon_count"]

    feature["off_hours_logons_deviation"] = (
        0 - baseline["off_hours_logons"]
    )

    feature["distinct_pcs_deviation"] = (
        1 - baseline["distinct_pcs"]
    )

    feature["usb_connects_deviation"] = (
        0 - baseline["usb_connects"]
    )

    feature["off_hours_usb_deviation"] = (
        0 - baseline["off_hours_usb"]
    )

    feature["files_copied_to_usb_deviation"] = (
        0 - baseline["files_copied_to_usb"]
    )

    feature["sensitive_files_to_usb_deviation"] = (
        0 - baseline["sensitive_files_to_usb"]
    )

    feature["total_emails_sent_deviation"] = (
        0 - baseline["total_emails_sent"]
    )

    feature["external_emails_sent_deviation"] = (
        0 - baseline["external_emails_sent"]
    )

    feature["total_attachments_deviation"] = (
        0 - baseline["total_attachments"]
    )

    feature["total_email_size_deviation"] = (
        0 - baseline["total_email_size"]
    )

    return pd.DataFrame([feature])