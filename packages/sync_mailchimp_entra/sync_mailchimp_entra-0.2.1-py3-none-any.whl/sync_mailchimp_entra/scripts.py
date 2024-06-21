import automationassets  # type: ignore
from sync_mailchimp_entra.core import sync
from sync_mailchimp_entra.core.mailchimp import MailchimpClient
from sync_mailchimp_entra.core.graph import GraphClient


async def main():
    # Config Graph
    GraphClient.get_instance(
        automationassets.get_automation_variable("TENANT_ID"),
        automationassets.get_automation_variable("APPLICATION_ID"),
        automationassets.get_automation_variable("APPLICATION_SECRET"),
        ["https://graph.microsoft.com/.default"],
    )
    entra_group_id = automationassets.get_automation_variable("ENTRA_GROUP_ID")

    # Config Mailchimp
    for i in range(
        1, int(automationassets.get_automation_variable("NB_MAILCHIMP")) + 1
    ):
        print(f"\nBeginning sync for Mailchimp {i}.")
        MailchimpClient.get_instance(
            automationassets.get_automation_variable("API_TOKEN_MAILCHIMP" + str(i)),
            automationassets.get_automation_variable("SERVER_PREFIX" + str(i)),
        )
        list_mailchimp_id = automationassets.get_automation_variable(
            "LIST_MAILCHIMP_ID" + str(i)
        )

        await sync.mailchimp_entra(list_mailchimp_id, entra_group_id)
        print(f"Sync for Mailchimp {i} finished.")
