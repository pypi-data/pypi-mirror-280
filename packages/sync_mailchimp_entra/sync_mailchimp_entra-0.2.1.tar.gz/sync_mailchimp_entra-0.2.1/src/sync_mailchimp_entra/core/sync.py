from sync_mailchimp_entra.core.mailchimp import MailchimpClient
from sync_mailchimp_entra.core.graph import GraphClient


async def mailchimp_entra(list_mailchimp_id, entra_group_id):
    members_mailchimp_emails = MailchimpClient.get_instance().list_mailchimp_emails(
        list_mailchimp_id
    )
    members_entra_emails = await GraphClient.get_instance().list_entra_emails(
        entra_group_id
    )

    for email in members_mailchimp_emails:
        if email not in members_entra_emails:
            MailchimpClient().get_instance().remove_member(list_mailchimp_id, email)

    for email in members_entra_emails:
        if email not in members_mailchimp_emails:
            user = await GraphClient.get_instance().get_user(email)

            # List of company names associated to languages
            if user.company_name == "XLM":
                language = "fr"
            else:
                language = "en"
            if user.given_name is None or user.surname is None:
                MailchimpClient().get_instance().add_member(
                    list_mailchimp_id, email, language=language
                )
            else:
                MailchimpClient().get_instance().add_member(
                    list_mailchimp_id,
                    email,
                    first_name=user.given_name,
                    last_name=user.surname,
                    language=language,
                )
