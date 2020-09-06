# Decision Log

Decisions made for this project will be tracked here in as ADRs using the MADR format. Information
about ADRs is available at https://adr.github.io/ and information on the MADR format specifically
is available at: https://adr.github.io/madr/.

## How to Add an ADR
Install [adr-tools](https://github.com/npryce/adr-tools) and [adr-log](https://github.com/adr/adr-log).

##### Create a new ADR file
Create a new ADR, e.g. a new ADR with the title "Use MySQL Database":

    adr new Use MySQL Database

Create a new ADR that supercedes ADR `#0012`:

    adr new -s 12 Use PostgreSQL Database

Create a new ADR that supercedes ADRs 3 and 4, and amends ADR 5:

    adr new -s 3 -s 4 -l "5:Amends:Amended by" Use Riak CRDTs to cope with scale


##### Write the ADR

##### Update the ADR log at `decision-log/index.md`

    adr-log -d docs/decision-log/ -i

Or manually update the list.

## Log
This log is the list of decisions made for the RTK Companion project.

<!-- adrlog -- Regenerate the content by using "adr-log -i". You can install it via "npm install -g adr-log" -->

<!-- adrlogstop -->
