# CSD Dash Notes Tool - Console Version
# This program helps CSD / Service Desk agents create notes
# that can be copied into Dash / ServiceNow.

# This function prints a blank line to make the program easier to read.
def print_blank_line():
    print()


# This function makes sure the user enters a KB Article Number.
# The KB Article Number is required for incident tickets.
def get_required_kb_article():
    kb_article = ""

    while kb_article == "":
        kb_article = input("Enter KB Article Number: ").strip()

        if kb_article == "":
            print("KB Article Number is required for incident tickets.")
            print("Please enter the KB Article Number before continuing.")
            print_blank_line()

    return kb_article


# This function collects all the information for the ticket note.
def get_ticket_information():
    print("CSD Dash Notes Tool")
    print("Create structured notes for Dash / ServiceNow")
    print("-------------------------------------------")
    print_blank_line()

    incoming_phone = input("Enter Incoming Phone Number: ").strip()
    customer_name = input("Enter Customer Name: ").strip()
    customer_eid = input("Enter Customer eID: ").strip()
    customer_email = input("Enter Customer Email: ").strip()
    customer_phone = input("Enter Customer Phone Number: ").strip()
    device_name = input("Enter Device Name / IP Address: ").strip()

    # KB Article Number is required, so we use a separate function for it.
    kb_article = get_required_kb_article()

    impact = input("Enter Impact: ").strip()
    urgency = input("Enter Urgency: ").strip()
    others_affected = input("Enter Others Affected? Yes/No/Unknown: ").strip()

    print_blank_line()
    issue = input("Enter Issue: ").strip()

    print_blank_line()
    who_was_contacted = input("Enter Who Was Contacted: ").strip()

    print_blank_line()
    troubleshooting_steps = input("Enter Troubleshooting Steps: ").strip()

    print_blank_line()
    result = input("Enter Result: ").strip()

    print_blank_line()
    next_step = input("Enter Next Step: ").strip()

    # We return all the answers so another function can build the note.
    return (
        incoming_phone,
        customer_name,
        customer_eid,
        customer_email,
        customer_phone,
        device_name,
        kb_article,
        impact,
        urgency,
        others_affected,
        issue,
        who_was_contacted,
        troubleshooting_steps,
        result,
        next_step
    )


# This function builds the final Dash / ServiceNow note.
def build_note(
    incoming_phone,
    customer_name,
    customer_eid,
    customer_email,
    customer_phone,
    device_name,
    kb_article,
    impact,
    urgency,
    others_affected,
    issue,
    who_was_contacted,
    troubleshooting_steps,
    result,
    next_step
):
    note = f"""
Incoming Phone Number:
{incoming_phone}

Issue:
{issue}

Impact:
{impact}

Urgency:
{urgency}

Others Affected?:
{others_affected}

Device Name/IP Address:
{device_name}

Customer's Name:
{customer_name}

Customer's eID:
{customer_eid}

Customer's Email:
{customer_email}

Customer's Phone Number:
{customer_phone}

KB Article Number:
{kb_article}

Who Was Contacted:
{who_was_contacted}

Troubleshooting Steps:
{troubleshooting_steps}

Result:
{result}

Next Step:
{next_step}
"""

    return note


# This is the main part of the program.
def main():
    ticket_information = get_ticket_information()

    note = build_note(
        ticket_information[0],
        ticket_information[1],
        ticket_information[2],
        ticket_information[3],
        ticket_information[4],
        ticket_information[5],
        ticket_information[6],
        ticket_information[7],
        ticket_information[8],
        ticket_information[9],
        ticket_information[10],
        ticket_information[11],
        ticket_information[12],
        ticket_information[13],
        ticket_information[14]
    )

    print_blank_line()
    print("Your Dash Note:")
    print("-------------------------------------------")
    print(note)
    print("-------------------------------------------")
    print("Copy the note above and paste it into Dash.")


# This tells Python to start the program.
main()