# Oracle_Data_Integrator
This guide will show you the resources to learn the basics of using ODI. 

![](77.png) 

## Recommended beginner tutorials
[How to use ODI lab](https://www.oracle.com/technetwork/middleware/data-integrator/overview/odi-12c-getting-started-guide-2032250.pdf)

[Flat file to database](https://www.oracle.com/webfolder/technetwork/tutorials/obe/fmw/odi/odi_12c/odi12c_exp_flat_2_tbl/odi12c_exp_flat_2_tbl.html#section1)

[How to install ODI](https://docs.oracle.com/en/middleware/fusion-middleware/data-integrator/12.2.1.3/odimp/using-oracle-data-integrator-oracle-cloud-marketplace.pdf)

[Oracle Data Integrator on OCI Marketplace](https://cloudmarketplace.oracle.com/marketplace/en_US/listing/59419903)

[Install ODI on VirtualBox](https://www.oracle.com/downloads/developer-vm/community-downloads.html#odi)

[Basics/Overview of ODI on Youtube](https://www.youtube.com/watch?v=Mtz9mEQRBXA)

## Use cases

### Reading files from remote servers
To read a file from a remote server, you must install an agent on that server so it can access the files.
[Install an agent on the server (details on how & why)](https://community.oracle.com/thread/3892184)

**Note:** Using an agent is not allowed with ODI Marketplace - in place of the agent you can create a VPN connection, whitelist the IP address of the compute node ODI is running on, and/or have FastConnect.

[Where to install agent](https://www.ateam-oracle.com/understanding-where-to-install-the-odi-standalone-agent)

**Note:** Again, this is not an option when solely using ODI in the cloud - you need an on-prem license as well. 

[How to install agent](https://docs.oracle.com/en/middleware/data-integrator/12.2.1.3/tutorial-creating-standalone-agent/)

### Connecting to SQL Server

To connect to SQL Server, it needs the JDBC driver & JRE installed on the SQL Server.

1. Download & install the JDBC driver for SQL Server:

[Download](https://www.microsoft.com/en-us/download/details.aspx?id=58505)

[JDBC Driver details](https://docs.microsoft.com/en-us/sql/connect/jdbc/download-microsoft-jdbc-driver-for-sql-server?view=sql-server-ver15)

[Getting started with the JDBC Driver](https://blogs.msdn.microsoft.com/brian_swan/2011/03/02/getting-started-with-the-sql-server-jdbc-driver/)

[Download & install the Java Runtime Environment for SQL Server connection](https://www.oracle.com/technetwork/java/javase/downloads/index.html)

2. Adding JDBC & JRE to the path where SQL Server runs:

[Using the JDBC Driver](https://docs.microsoft.com/en-us/sql/connect/jdbc/using-the-jdbc-driver?view=sql-server-ver15)

[Setting the JAVA_HOME variable in windows](https://confluence.atlassian.com/doc/setting-the-java_home-variable-in-windows-8895.html)

[SQL Server knowledge modules](https://docs.oracle.com/html/E12644_03/ms_sqlserver.htm#BGBHDDGB)

[General JDBC driver notes](https://docs.microsoft.com/en-us/sql/connect/jdbc/overview-of-the-jdbc-driver?view=sql-server-ver15)

3. Connecting to SQL Server on ODI (extra documentation):

[Knowledge modules for SQL Server on ODI](https://docs.oracle.com/middleware/1212/odi/ODIKM/ms_sqlserver.htm#ODIKM957)

[Sample JDBC url](https://docs.microsoft.com/en-us/sql/connect/jdbc/connection-url-sample?view=sql-server-ver15)

[Connecting with the JDBC Driver](https://docs.microsoft.com/en-us/sql/connect/jdbc/connecting-to-sql-server-with-the-jdbc-driver?view=sql-server-ver15)

[Connecting to SQL Server](https://docs.oracle.com/html/E12644_03/ms_sqlserver.htm#BGBHDDGB)

### Other use cases
1. [You can execute SSIS packages from SQL Server stored procedures](https://www.mssqltips.com/sqlservertip/2992/how-to-execute-an-integration-services-ssis-package-from-a-sql-server-stored-procedure/)

2. [More SSIS information](https://docs.microsoft.com/en-us/sql/integration-services/deploy-and-execute-ssis-packages-using-stored-procedures?view=sql-server-2014)

3. Salesforce connects via JDBC as well

  This is the syntax for salesforce's JDBC connection under physical topology:
```     

jdbc.weblogic:sforce//login.salesforce.com;User=email@email.com;Password=password12345;SecurityToken=6gaFzpiuetpyubD6Yhadk;ljadDTlNKpX

```
[More salesforce information](https://blogs.perficient.com/2016/09/14/odi-integration-with-salesforce/)

4. More information on the agent

[Learn about ODI agents](https://blogs.oracle.com/dataintegration/learn-about-oracle-data-integrator-odi-agents)

[Where to install the standalone agent](https://www.ateam-oracle.com/understanding-where-to-install-the-odi-standalone-agent)

[Differences between the agents](https://www.ateam-oracle.com/odi-agents-standalone-jee-and-colocated)

[Creating a standalone agent](https://docs.oracle.com/en/middleware/fusion-middleware/tutorial-creating-standalone-agent/#CreatingaLogicalAgent)

[Setting up the ODI agent](https://www.oracle.com/webfolder/technetwork/tutorials/obe/fmw/odi/odi_11g/setup_odi_agent/setup_odi_agent.htm)

[Colocated agent](https://gerardnico.com/dit/odi/agent#colocated)

[What is the ODI agent?](https://dzone.com/articles/odi-11g-odi-12c-whats-an-agent)

[Differences between agent types](https://stackoverflow.com/questions/51043048/what-is-the-significance-of-localno-agent-standalone-java-agent-in-odi)

[Local(no agent](https://www.databaseusers.com/article/6349392/local(No+agent)+vs+OracleDIAgent)

[The Standalone-Collocated Agent](https://www.kpipartners.com/blog/bid/157960/The-Oracle-Data-Integrator-12C-Standalone-Collocated-Agent)






