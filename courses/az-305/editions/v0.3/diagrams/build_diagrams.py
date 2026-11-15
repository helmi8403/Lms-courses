from pathlib import Path
import base64,html,subprocess,json,re
import xml.etree.ElementTree as ET
ET.register_namespace("", "http://www.w3.org/2000/svg")
root=Path(__import__('os').environ.get('AZURE_ICON_ROOT', 'Azure_Public_Service_Icons/Icons'))
out=Path(__file__).resolve().parent;out.mkdir(exist_ok=True)
used={}
serial=0
def icon(key):
 fs=list(root.rglob('*icon-service-'+key+'.svg'))
 assert fs,key
 p=fs[0];used[key]=str(p.relative_to(root));return p.read_text()
def native_icon(key,x,y):
 global serial
 serial+=1
 raw=icon(key)
 for ident in re.findall(r'id="([^"]+)"',raw):
  raw=raw.replace('id="'+ident+'"','id="n'+str(serial)+'_'+ident+'"').replace('#'+ident,'#n'+str(serial)+'_'+ident)
 e=ET.fromstring(raw);e.set('x',str(x-43));e.set('y',str(y-43));e.set('width','86');e.set('height','86')
 return ET.tostring(e,encoding='unicode')
def text(x,y,t,size=23,fill='#16334c',anchor='middle',weight='400'):
 return f'<text x="{x}" y="{y}" font-family="DejaVu Sans" font-size="{size}" fill="{fill}" text-anchor="{anchor}" font-weight="{weight}">{html.escape(t)}</text>'
def base(title,subtitle):
 return ['<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="1800" height="1000" viewBox="0 0 1800 1000"><defs><marker id="arrow" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6" fill="none" stroke="#327fa5" stroke-width="1.5"/></marker></defs><rect width="1800" height="1000" fill="#f6fafc"/><path d="M0 0H1800V160H0Z" fill="#102d48"/>',text(70,68,title,38,'#ffffff','start','700'),text(70,116,subtitle,22,'#b9dfec','start')]
def zone(a,x,y,w,h,label,color='#e7f2f8'):
 a.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="34" fill="{color}" stroke="#9ac3d5" stroke-width="2"/>');a.append(text(x+28,y+39,label,20,'#436777','start','700'))
def node(a,x,y,key,label,sub=''):
 a.append(f'<circle cx="{x}" cy="{y}" r="65" fill="white"/>')
 if key:a.append(native_icon(key,x,y))
 else:
  a.append(f'<path d="M{x-35} {y+30}V{y-25}L{x} {y-42}L{x+35} {y-25}V{y+30}Z M{x-20} {y-10}H{x-10} M{x+10} {y-10}H{x+20} M{x-20} {y+8}H{x-10} M{x+10} {y+8}H{x+20}" fill="none" stroke="#52798f" stroke-width="5"/>')
 a.append(text(x,y+94,label,24,weight='700'))
 if sub:a.append(text(x,y+124,sub,18,'#476a80'))
def edge(a,x1,y1,x2,y2,label='',lx=None,ly=None,dash=False):
 a.append(f'<path d="M{x1},{y1} C{(x1+x2)/2},{y1} {(x1+x2)/2},{y2} {x2},{y2}" stroke="#327fa5" fill="none" stroke-width="3" marker-end="url(#arrow)" '+('stroke-dasharray="10 7"' if dash else '')+'/>')
 if label:
  xx=(x1+x2)/2 if lx is None else lx;yy=(y1+y2)/2-14 if ly is None else ly
  a.append(text(xx,yy,label,19,'#245b78'))
def note(a,lines):
 for i,l in enumerate(lines):a.append(text(70,865+i*29,l,21,'#284e66','start'))
def save(a,name):
 a.append(text(70,970,'Original teaching architecture • Microsoft Azure service icons, unmodified • not a deployed system',17,'#5a7484','start'))
 a.append('</svg>');f=out/(name+'.svg');f.write_text(''.join(a));subprocess.run(['inkscape',str(f),'--export-type=png','--export-filename='+str(out/(name+'.png'))],capture_output=True,check=True)
#1
x=base('01  Identity: directory sync and workload access','Separate synchronization from authorization. Each lane represents a different responsibility.')
zone(x,60,200,1680,250,'HYBRID WORKFORCE DIRECTORY')
node(x,230,320,None,'On-premises AD DS');node(x,820,320,'Entra-Connect-Sync','Entra Connect Sync');node(x,1440,320,'Tenant-Properties','Entra workforce tenant')
edge(x,310,320,740,320,'Directory synchronization');edge(x,900,320,1360,320,'Identity / configured hash sync')
zone(x,60,490,1680,300,'APPLICATION DATA ACCESS','#edf4ec')
node(x,240,640,'App-Services','App Service');node(x,790,620,'Entra-Managed-Identities','Managed identity','Assigned identity; no app secret')
node(x,1440,620,'Key-Vaults','Key Vault','Explicit data-plane permission')
edge(x,320,620,710,620,'Identity association',dash=True);edge(x,870,620,1360,620,'Token-authorized access')
note(x,['Directory synchronization does not itself grant application access. Conditional Access and role design remain separate.', 'Workload lane is conceptual: token issuance and network/DNS dependencies are omitted, not unnecessary.'])
save(x,'01-identity-hybrid')
#2
x=base('02  Private data path: a real network boundary','A regional VM-based example. Public application traffic is not direct database access.')
zone(x,365,210,1060,590,'AZURE VIRTUAL NETWORK / REGIONAL APPLICATION')
node(x,160,390,'Users','Internet clients');node(x,535,390,'Application-Gateways','Application Gateway','WAF_v2 candidate')
node(x,950,390,'Virtual-Machine','Application VMs','Separate application subnet');node(x,1280,620,'Private-Endpoints','Private endpoint')
node(x,1620,620,'SQL-Database','Azure SQL Database');node(x,870,650,'DNS-Zones','Private DNS','Resolution linked to VNet')
edge(x,235,390,455,390,'HTTPS');edge(x,615,390,870,390,'Application HTTPS');edge(x,1020,420,1210,585,'SQL connection',lx=1165,ly=480)
edge(x,1360,620,1540,620,'Private access');edge(x,950,650,1200,650,'Name resolution',dash=True)
note(x,['Public database access must be separately configured; a private endpoint alone does not disable it.', 'NSGs, outbound connectivity, identity and certificates are separate controls. DNS determines the resolved destination.'])
save(x,'02-network-private-data')
#3
x=base('03  Web request and background command paths','Keep the authoritative transaction separate from asynchronous notification work.')
zone(x,60,200,1680,245,'SYNCHRONOUS REQUEST PATH')
node(x,200,315,'Front-Door-and-CDN-Profiles','Azure Front Door');node(x,820,315,'App-Services','App Service API');node(x,1440,315,'SQL-Database','Booking database')
edge(x,280,315,740,315,'HTTPS origin request');edge(x,900,315,1360,315,'Authoritative transaction')
zone(x,60,490,1680,300,'ASYNCHRONOUS COMMAND PATH','#edf4ec')
node(x,240,630,'Azure-Service-Bus','Service Bus','Tier supports required controls');node(x,830,630,'Function-Apps','Functions worker','Hosting chosen for workload');node(x,1450,630,None,'Notification provider')
edge(x,820,445,240,550,'Publish durable work',lx=500,ly=475);edge(x,320,630,750,630,'Receive / settle');edge(x,910,630,1370,630,'Provider API call')
note(x,['Database commit and message publication require an explicit consistency strategy; the drawing does not imply atomicity.', 'Duplicate delivery and provider timeouts need idempotency / reconciliation. A queued command is not completed work.'])
save(x,'03-app-command-architecture')
#4
x=base('04  Operational data becomes a reporting product','A scheduled analytical path fits a weekly report; it need not burden transaction queries.')
zone(x,60,220,490,550,'OPERATIONAL SOURCES');zone(x,600,220,1140,550,'CURATED ANALYTICAL PATH','#edf4ec')
node(x,300,365,'SQL-Database','Operational SQL');node(x,300,635,'Storage-Accounts','Document objects')
node(x,795,430,'Data-Factories','Data Factory','Orchestration + movement');node(x,1210,430,'Storage-Accounts','Data lake storage','ADLS Gen2 configured account')
node(x,1530,630,'Azure-Synapse-Analytics','Analytical serving','Example: Synapse workload')
edge(x,380,365,715,405,'Scheduled extraction');edge(x,380,635,715,460,'Approved object inputs',lx=540,ly=590)
edge(x,875,430,1130,430,'Curate / transform');edge(x,1290,430,1470,570,'Prepared data',lx=1430,ly=480)
note(x,['This is one analytical option, not a claim that Synapse is always preferable to Fabric or Databricks.', 'Identity, lineage, quality and retention apply at each boundary. The document store icon is not a warehouse.'])
save(x,'04-data-analytics')
#5
x=base('05  Regional continuity is not historical recovery','The example separates asynchronous geo-replication from recovering an earlier data state.')
zone(x,60,210,770,555,'PRIMARY REGION');zone(x,970,210,770,555,'SECONDARY REGION','#edf4ec')
node(x,260,345,'App-Services','Primary application');node(x,1260,345,'App-Services','Recovery application','Capacity / config required')
node(x,540,610,'SQL-Database','Primary SQL');node(x,1260,610,'SQL-Database','Geo-secondary SQL')
edge(x,335,345,500,535,'Transaction path',lx=390,ly=510);edge(x,620,610,1180,610,'Asynchronous geo-replication',ly=580,dash=True)
node(x,680,350,'Storage-Accounts','Historical backups','Separate retention / restore')
edge(x,610,580,760,360,'Backup protection',lx=760,ly=515,dash=True)
edge(x,1340,345,1340,560,'Recovery data path',lx=1510,ly=505)
note(x,['Failover groups / client reconnect behavior and routing must be designed. Replication can propagate a bad update.', 'RTO includes detection, decision and validation; RPO depends on the recovery point. No recovery timing is proven here.'])
save(x,'05-ha-dr')
#6
x=base('06  Observability: three evidence paths, one response model','Application traces, guest collection and platform logs are not the same source.')
zone(x,60,200,490,590,'EVIDENCE SOURCES');zone(x,600,200,1140,590,'COLLECTION • ANALYSIS • RESPONSE','#edf4ec')
node(x,290,335,'App-Services','Application');node(x,290,625,'Virtual-Machine','Virtual machine')
node(x,790,335,'Application-Insights','Application Insights','Supported OTel instrumentation');node(x,790,625,'Data-Collection-Rules','Data collection rule','Supported agent / ingestion path')
node(x,1240,480,'Log-Analytics-Workspaces','Log Analytics','Table plan + retention choice');node(x,1590,480,'Alerts','Alerts / response','Action groups configured')
edge(x,370,335,710,335,'Traces / requests');edge(x,370,625,710,625,'Guest telemetry')
edge(x,870,365,1160,450,'Workspace-based data');edge(x,870,595,1160,510,'Collect / transform / route')
edge(x,1320,480,1510,480,'Alert signal')
note(x,['Resource diagnostic settings route supported platform logs separately. DCRs do not replace every diagnostic setting.', 'Redaction, collection health and access matter. A dashboard with no errors but no traffic is not proof of service health.'])
save(x,'06-monitoring')
(out/'ICON-MANIFEST.json').write_text(json.dumps(used,indent=2))
print(out)
