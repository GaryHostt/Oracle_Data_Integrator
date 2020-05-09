# Oracle_Data_Integrator


![](pic.png)

<p align="center">
  <img src="https://github.com/GaryHostt/Oracle_Data_Integrator/blob/master/pic.png?raw=true" alt="ODI"/>
</p>

This guide will show you the resources to learn the basics of using ODI. 

Here is the main [ODI documentation](https://docs.oracle.com/en/middleware/fusion-middleware/data-integrator/12.2.1.4/index.html).

Here is the [12.2.1.3 documentation](https://docs.oracle.com/en/middleware/fusion-middleware/data-integrator/12.2.1.3/odimp/getting-started-oracle-cloud-marketplace.html#GUID-1793F6A6-8581-465D-BBE3-8F0C8ADD6536).

Get started by spinning up [Oracle Data Integrator on OCI Marketplace](https://cloudmarketplace.oracle.com/marketplace/en_US/listing/59419903) or by spinning up [ODI Studio on VirtualBox](https://www.oracle.com/downloads/developer-vm/community-downloads.html#odi).

[What's new in ODI 12c?](http://www.oracle.com/us/products/middleware/data-integration/odi-12c-new-features-wp-122140-5762948.pdf)

## Getting started

[How to install ODI from the marketplace](https://www.ateam-oracle.com/deploying-oracle-data-integrator-marketplace-in-a-public-subnet-with-autonomous-database)

[How to install ODI from the marketplace (alternative)](https://docs.oracle.com/en/middleware/fusion-middleware/data-integrator/12.2.1.3/odimp/using-oracle-data-integrator-oracle-cloud-marketplace.pdf)

If you're starting from scratch, use the above two links to get yourself ODI on OCI. You use will use [Resource Manager](https://docs.cloud.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/resourcemanager.htm) on OCI to manage your deployments with terraform.

[Flat file to database](https://www.oracle.com/webfolder/technetwork/tutorials/obe/fmw/odi/odi_12c/odi12c_exp_flat_2_tbl/odi12c_exp_flat_2_tbl.html#section1) - beginner

[How to use ODI lab](https://www.oracle.com/technetwork/middleware/data-integrator/overview/odi-12c-getting-started-guide-2032250.pdf) - advanced

The above two workshops are the best places to get started using ODI before proceeding with more complex use cases below.

[VNCViewer](https://www.realvnc.com/en/connect/download/viewer/windows/) or [TigerVNC](https://tigervnc.org/)

After spinning up ODI on OCI, you will need one of the two above in order to see the Linux & ODI GUI.

[Basics/Overview of ODI on Youtube](https://www.youtube.com/watch?v=Mtz9mEQRBXA)

[ODI Learning Tutorials](https://blogs.oracle.com/dataintegration/data-integration-platform-cloud-for-saas-applications)

## ODI with BICC, ADW, OCI object storage

In general, for users seeking to extract high volumes (or incremental) of data from Fusion, they can use BICC to send extracts to Oracle object storage. ODI can then read the CSVs from there and write them to the target database of your choice. Details on this usage parttern are explained below. However, [data can also be extracted with ODI via BI Publisher reports](https://docs.oracle.com/en/middleware/fusion-middleware/data-integrator/12.2.1.4/odikm/oracle-enterprise-resource-planning-cloud.html#GUID-9D29A5CB-00A4-4033-B63C-31EF8123276A).

[Using an autonomous database as your Repository](https://medium.com/@zzhangjii/configure-autonomous-database-adb-as-repo-for-oracle-data-integrator-odi-3d1a3dba412e)

While the marketplace image comes with an embedded MySQL database which can be used for your ODI repository, the above documentation shows how to use an Autonomous Database instead to take advantage its Oracle-managed features. 

[Complete guide on the ODI marketplace + BICC + object storage + Autonomous Database](https://www.ateam-oracle.com/reference-architecture-fusion-saas-data-replication-into-adw-%3A-using-odi-marketplace-and-bicc)

[Manipulating Data from Object Storage to ADW using ODI](https://blogs.oracle.com/dataintegration/manipulating-data-from-oracle-object-storage-to-oracle-autonomous-data-warehouse-adw-with-oracle-data-integrator-odi)

[Using object storage with ODI](https://docs.oracle.com/en/middleware/fusion-middleware/data-integrator/12.2.1.4/odikm/oracle-object-storage.html#GUID-DFE3EBF0-0A0D-4BA0-94FE-202185E47804)

[Connecting to object storage with ODI + screenshots](https://blogs.oracle.com/dataintegration/manipulating-data-from-oracle-object-storage-to-oracle-autonomous-data-warehouse-adw-with-oracle-data-integrator-odi)

[Moving data to ADW](https://blogs.oracle.com/dataintegration/loading-data-into-oracle-autonomous-data-warehouse-cloud-with-oracle-data-integration)

[Using BICC with ODI](https://docs.oracle.com/en/middleware/fusion-middleware/data-integrator/12.2.1.4/odikm/oracle-business-intelligence-cloud-connector.html#GUID-57D29056-3FBF-41B8-9F2A-C38B1556983F)

While you can work with BICC extracts if they are being written to object storage, you can also work with BICC from the UCM Server on Fusion applications.

[Using ADW with ODI](https://docs.oracle.com/en/middleware/fusion-middleware/data-integrator/12.2.1.4/odikm/oracle-autonomous-data-warehouse-cloud.html#GUID-4C242603-09C4-464F-B299-2F21C67D1E43)

## More Use cases

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

### Reading files from remote servers
To read a file from a remote server, you must install an agent on that server so it can access the files.
[Install an agent on the server (details on how & why)](https://community.oracle.com/thread/3892184)

**Note:** Using an agent is not allowed with ODI Marketplace - in place of the agent you can create a VPN connection, whitelist the IP address of the compute node ODI is running on, and/or have FastConnect.

[Where to install agent](https://www.ateam-oracle.com/understanding-where-to-install-the-odi-standalone-agent)

**Note:** Again, this is not an option when solely using ODI in the cloud - you need an on-prem license as well. 

[How to install agent](https://docs.oracle.com/en/middleware/data-integrator/12.2.1.3/tutorial-creating-standalone-agent/)

### Other use cases
1. [You can execute SSIS packages from SQL Server stored procedures](https://www.mssqltips.com/sqlservertip/2992/how-to-execute-an-integration-services-ssis-package-from-a-sql-server-stored-procedure/)

2. [More SSIS information](https://docs.microsoft.com/en-us/sql/integration-services/deploy-and-execute-ssis-packages-using-stored-procedures?view=sql-server-2014)

3. Salesforce connects via JDBC as well

  This is the syntax for salesforce's JDBC connection under physical topology:
```     

jdbc.weblogic:sforce//login.salesforce.com;User=email@email.com;Password=password12345;SecurityToken=6gaFzpiuetpyubD6Yhadk;ljadDTlNKpX

```

[More salesforce information](https://blogs.perficient.com/2016/09/14/odi-integration-with-salesforce/)

4. [Setting up scenarios & plans](https://blogs.perficient.com/2014/09/02/creating-oracle-data-integrator-odi-scenario-and-load-plan/)

5. More information on the agent

[Learn about ODI agents](https://blogs.oracle.com/dataintegration/learn-about-oracle-data-integrator-odi-agents)

[Where to install the standalone agent](https://www.ateam-oracle.com/understanding-where-to-install-the-odi-standalone-agent)

[Differences between the agents](https://www.ateam-oracle.com/odi-agents-standalone-jee-and-colocated)

[Creating a standalone agent](https://docs.oracle.com/en/middleware/fusion-middleware/tutorial-creating-standalone-agent/#CreatingaLogicalAgent)

[Setting up the ODI agent](https://www.oracle.com/webfolder/technetwork/tutorials/obe/fmw/odi/odi_11g/setup_odi_agent/setup_odi_agent.htm)

[Colocated agent](https://gerardnico.com/dit/odi/agent#colocated)

[What is the ODI agent?](https://dzone.com/articles/odi-11g-odi-12c-whats-an-agent)

[Differences between agent types](https://stackoverflow.com/questions/51043048/what-is-the-significance-of-localno-agent-standalone-java-agent-in-odi)

[Local(no agent)](https://www.databaseusers.com/article/6349392/local(No+agent)+vs+OracleDIAgent)

[The Standalone-Collocated Agent](https://www.kpipartners.com/blog/bid/157960/The-Oracle-Data-Integrator-12C-Standalone-Collocated-Agent)

### Misc

[File mapping project - youtube](https://www.youtube.com/watch?v=B7hyh3QPsLs)

[How to recover supervisor password](https://odielt.wordpress.com/2017/03/01/how-to-supervisor-password-in-odi/)

[Create an API key for OCI user](https://docs.cloud.oracle.com/en-us/iaas/Content/API/Concepts/apisigningkey.htm)

The above is requisite for connecting to object storage with ODI.

```
ssh-keygen -t rsa -b 2048
```
This is a bash command that can be used to generate ssh keys for the compute node where the marketplace image runs. If you give them to another user to connect, that user needs to run 'chmod 400' on that key after receiving it.





