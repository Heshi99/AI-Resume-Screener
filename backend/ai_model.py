from sentence_transformers import SentenceTransformer, util
import spacy

# Load models
model = SentenceTransformer('all-MiniLM-L6-v2')
nlp = spacy.load("en_core_web_sm")

TECH_KEYWORDS = {
     'Python', 'Java', 'C', 'C++', 'C#', 'JavaScript', 'TypeScript', 'Ruby', 'PHP', 'HTML', 
    'CSS', 'SQL', 'NoSQL', 'React', 'Angular', 'Vue.js', 'Node.js', 'Express.js', 'Django', 
    'Flask', 'Spring', 'ASP.NET', 'JSP', 'Ruby on Rails', 'Swift', 'Kotlin', 'Objective-C', 
    'Android', 'iOS', 'Git', 'GitHub', 'GitLab', 'Bitbucket', 'Docker', 'Kubernetes', 'Jenkins', 
    'CI/CD', 'AWS', 'Azure', 'Google Cloud', 'Heroku', 'Terraform', 'Ansible', 'Puppet', 'Chef', 
    'Linux', 'Windows', 'Unix', 'MacOS', 'Shell Scripting', 'Bash', 'PowerShell', 'Vim', 'Emacs', 
    'Apache', 'Nginx', 'MySQL', 'PostgreSQL', 'MongoDB', 'Redis', 'Elasticsearch', 'SQLite', 
    'Oracle', 'DB2', 'Big Data', 'Hadoop', 'Spark', 'Kafka', 'ETL', 'Machine Learning', 'Deep Learning', 
    'AI', 'Natural Language Processing', 'TensorFlow', 'PyTorch', 'Keras', 'Scikit-learn', 'Pandas', 
    'NumPy', 'Matplotlib', 'Seaborn', 'OpenCV', 'SQLAlchemy', 'Jupyter', 'Data Science', 'Data Analysis', 
    'Data Visualization', 'Tableau', 'Power BI', 'Excel', 'SAS', 'R', 'MATLAB', 'Google Analytics', 
    'BI Tools', 'Data Warehousing', 'Data Mining', 'Web Scraping', 'API', 'RESTful API', 'GraphQL', 
    'OAuth', 'JWT', 'SOAP', 'XML', 'JSON', 'Web Services', 'Swagger', 'Postman', 'JUnit', 'TestNG', 
    'Selenium', 'Appium', 'Jenkins', 'Docker', 'Vagrant', 'Microservices', 'MVC', 'MVVM', 'TDD', 
    'BDD', 'Scrum', 'Agile', 'Kanban', 'JIRA', 'Confluence', 'Trello', 'Asana', 'Slack', 'Basecamp', 
    'Cloud Computing', 'DevOps', 'SysAdmin', 'Network Administration', 'Firewall', 'VPN', 'DNS', 
    'DHCP', 'TCP/IP', 'NAT', 'HTTP', 'HTTPS', 'FTP', 'SSH', 'SFTP', 'Wireshark', 'Wi-Fi', 'VPN', 
    'Load Balancer', 'DNS', 'BGP', 'Routing', 'Switching', 'OSI Model', 'Wi-Fi', 'Networking Protocols', 
    'AWS Lambda', 'Google Functions', 'Microservices Architecture', 'Monolithic Architecture', 
    'Docker Compose', 'Kubernetes', 'CloudFormation', 'Amazon EC2', 'Amazon S3', 'IAM', 'Elastic Load Balancing', 
    'Auto Scaling', 'Amazon RDS', 'Amazon VPC', 'Elastic Beanstalk', 'CloudWatch', 'Route 53', 'Redshift', 
    'BigQuery', 'Cloud Storage', 'S3', 'Google Cloud Storage', 'Firebase', 'Lambda', 'Cognito', 'DynamoDB', 
    'Elasticsearch', 'Cassandra', 'HBase', 'ClickHouse', 'Time Series Databases', 'AWS SDK', 'Firebase SDK', 
    'Data Lakes', 'Serverless Computing', 'Blockchain', 'Ethereum', 'Solidity', 'Cryptography', 'Cryptocurrency', 
    'Bitcoin', 'Smart Contracts', 'Docker Swarm', 'Docker Compose', 'Containerization', 'Virtualization', 
    'VPS', 'VMware', 'Hyper-V', 'Vagrant', 'GitOps', 'Ansible', 'Chef', 'Terraform', 'Puppet', 'Scripting', 
    'Automation', 'Monitoring', 'Log Management', 'Prometheus', 'Grafana', 'Zabbix', 'Nagios', 'New Relic', 
    'Datadog', 'CloudWatch', 'SolarWinds', 'JMeter', 'Load Testing', 'Performance Testing', 'UAT', 'Test Automation', 
    'Unit Testing', 'Integration Testing', 'Acceptance Testing', 'Regression Testing', 'Load Testing', 'Stress Testing', 
    'Functional Testing', 'Non-Functional Testing', 'API Testing', 'Performance Tuning', 'Profiling', 'Database Optimization', 
    'Indexing', 'Query Optimization', 'Sharding', 'Replication', 'Backup and Recovery', 'High Availability', 
    'Disaster Recovery', 'ElasticSearch', 'MySQL Performance', 'Data Consistency', 'Data Integrity', 
    'Database Design', 'Normalization', 'Denormalization', 'Entity Relationship Diagram', 'SQL Server', 'T-SQL', 
    'NoSQL Databases', 'Schema Design', 'Data Security', 'Data Encryption', 'Authentication', 'Authorization', 
    'RBAC', 'LDAP', 'OAuth 2.0', 'Single Sign-On', 'Two-Factor Authentication', 'MFA', 'Active Directory', 
    'Cloud Identity', 'IAM', 'Identity Federation', 'SAML', 'OAuth', 'JWT', 'PKI', 'Public Key Infrastructure', 
    'X.509', 'SFTP', 'TLS', 'SSL', 'HTTPS', 'TLS/SSL Protocol', 'Cryptographic Hash Functions', 'AES', 'RSA', 'TLS', 
    'PKI', 'FIDO2', 'SCADA', 'IoT', 'Edge Computing', 'Virtual Reality', 'Augmented Reality', '3D Modeling', 
    'Unity', 'Unreal Engine', 'Blender', 'Autocad', 'CAD', '3D Graphics', 'HoloLens', 'IoT Protocols', 
    'MQTT', 'CoAP', 'Zigbee', 'Bluetooth', 'BLE', 'LoRaWAN', 'LPWAN', '5G', 'Cellular Networks', 'Smart Home', 
    'Edge Devices', 'Embedded Systems', 'Raspberry Pi', 'Arduino', 'FPGA', 'Microcontrollers', 'RTOS', 'Embedded C', 
    'Low-level Programming', 'Device Drivers', 'PCB Design', 'Firmware', 'IoT Security', 'Cybersecurity', 
    'Penetration Testing', 'Ethical Hacking', 'Red Team', 'Blue Team', 'SOC', 'SIEM', 'Firewall Management', 
    'Intrusion Detection System', 'Intrusion Prevention System', 'Malware Analysis', 'Forensics', 'Ransomware', 
    'Vulnerability Assessment', 'Risk Assessment', 'PCI-DSS', 'HIPAA', 'GDPR', 'ISO 27001', 'SOC 2', 'Incident Response', 
    'Threat Intelligence', 'DDoS Protection', 'Anti-virus', 'Data Loss Prevention', 'Network Segmentation', 
    'Security Audits', 'Security Policies', 'Cloud Security', 'Zero Trust', 'IDS', 'IPS', 'SIEM', 'Security Operations', 
    'Web Security', 'XSS', 'SQL Injection', 'Cross-site Request Forgery', 'CSRF', 'Malware Protection', 
    'RAT', 'Spyware', 'Trojan', 'Rootkits', 'Virus', 'Botnets', 'Ransomware', 'Cryptojacking', 'Phishing', 
    'Spear Phishing', 'Social Engineering', 'Network Security', 'Wi-Fi Security', 'Firewall Configuration', 
    'VPN Setup', 'Penetration Testing', 'Security Testing', 'Security Best Practices', 'Threat Hunting', 
    'Endpoint Security', 'Network Traffic Analysis', 'Advanced Persistent Threats', 'DNS Spoofing', 'DNSSEC', 
    'Packet Sniffing', 'Port Scanning', 'DNS Tunneling', 'HTTP Security', 'SSL/TLS', 'Secure Coding', 
    'Security Frameworks', 'NIST', 'OWASP', 'CIS', 'ISO/IEC 27001', 'Cloud-native Security', 'Kubernetes Security', 
    'Container Security', 'DevSecOps', 'Threat Modeling', 'Risk Management', 'Access Control', 'Business Continuity', 
    'Disaster Recovery', 'Breach Detection', 'Data Encryption', 'Data Backup', 'Data Masking', 'Data Anonymization', 
    'Compliance', 'Regulatory Compliance', 'PCI Compliance', 'GDPR Compliance', 'HIPAA Compliance', 
    'SOX Compliance', 'ISO Certification', 'Privacy Policy', 'Risk Management', 'Compliance Audits', 'Asset Management'}

TECH_KEYWORDS = set(map(str.lower, TECH_KEYWORDS))



def extract_skills_with_spacy(text):
    doc = nlp(text)
    skills = set()

    for token in doc:
        word = token.text.strip().lower()
        if word in TECH_KEYWORDS:
            skills.add(word)

    for chunk in doc.noun_chunks:
        chunk_text = chunk.text.strip().lower()
        if chunk_text in TECH_KEYWORDS:
            skills.add(chunk_text)

    return list(skills)




def get_resume_score_and_skills(jd_text, resume_text):
    # Embedding similarity
    
    jd_embedding = model.encode(jd_text, convert_to_tensor=True)
    resume_embedding = model.encode(resume_text, convert_to_tensor=True)
    similarity_score = util.cos_sim(jd_embedding, resume_embedding).item() * 100

    # Extract skills from both
    
    resume_skills = extract_skills_with_spacy(resume_text)
    jd_skills = extract_skills_with_spacy(jd_text)

    # Match / Suggest
    
    matched_skills = list(set(jd_skills) & set(resume_skills))
    missing_skills = list(set(jd_skills) - set(resume_skills))

    suggestions = {
        "matched": matched_skills,
        "missing": missing_skills
    }

    return similarity_score, resume_skills, suggestions