import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import time
import threading
import random

class RansomwareEducationSimulator:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Educational Ransomware Simulation - Cybersecurity Learning Tool")
        self.root.geometry("1000x700")
        self.root.configure(bg='#E8F4FD')
        self.root.resizable(True, True)
        
        # Color scheme - bright and educational
        self.colors = {
            'primary': '#2E86AB',      # Blue
            'secondary': '#A23B72',    # Purple
            'accent': '#F18F01',       # Orange
            'success': '#C73E1D',      # Red (for warnings)
            'background': '#E8F4FD',   # Light blue
            'text': '#2C3E50',         # Dark blue-gray
            'warning': '#E74C3C',      # Bright red
            'safe': '#27AE60'          # Green
        }
        
        self.current_phase = 0
        self.knowledge_score = 0
        self.setup_main_interface()
        
    def setup_main_interface(self):
        # Header
        header_frame = tk.Frame(self.root, bg=self.colors['primary'], height=80)
        header_frame.pack(fill='x', padx=10, pady=5)
        header_frame.pack_propagate(False)
        
        title_label = tk.Label(
            header_frame, 
            text="🛡️ RANSOMWARE EDUCATION SIMULATOR 🛡️",
            font=('Arial', 18, 'bold'),
            bg=self.colors['primary'],
            fg='white'
        )
        title_label.pack(expand=True)
        
        # Main content area
        self.main_frame = tk.Frame(self.root, bg=self.colors['background'])
        self.main_frame.pack(fill='both', expand=True, padx=10, pady=5)
        
        self.show_introduction()
    
    def show_introduction(self):
        self.clear_main_frame()
        
        # Introduction content
        intro_frame = tk.Frame(self.main_frame, bg=self.colors['background'])
        intro_frame.pack(fill='both', expand=True, padx=20, pady=20)
        
        welcome_label = tk.Label(
            intro_frame,
            text="Welcome to the Ransomware Education Simulator!",
            font=('Arial', 16, 'bold'),
            bg=self.colors['background'],
            fg=self.colors['text']
        )
        welcome_label.pack(pady=10)
        
        # Educational content
        education_text = """
🎯 LEARNING OBJECTIVES:
By the end of this simulation, you will understand:

✅ What ransomware is and how it works
✅ Common attack vectors and entry points
✅ Impact on individuals and organizations
✅ Prevention strategies and best practices
✅ Response procedures if attacked
✅ Recovery methods and backup importance

⚠️ IMPORTANT DISCLAIMER:
This is a 100% SAFE educational simulation. No actual files will be encrypted or harmed.
All activities are simulated for learning purposes only.

📚 WHAT IS RANSOMWARE?
Ransomware is malicious software that encrypts files on a victim's computer or network,
making them inaccessible. Attackers then demand payment (ransom) for the decryption key.

💡 WHY LEARN ABOUT RANSOMWARE?
• Ransomware attacks increased by 41% in 2022
• Average cost of a ransomware attack: $4.54 million
• 66% of organizations were hit by ransomware in 2022
• Knowledge is your best defense!
        """
        
        text_widget = scrolledtext.ScrolledText(
            intro_frame,
            wrap=tk.WORD,
            width=80,
            height=20,
            font=('Arial', 11),
            bg='white',
            fg=self.colors['text'],
            relief='ridge',
            bd=2
        )
        text_widget.pack(pady=10, fill='both', expand=True)
        text_widget.insert('1.0', education_text)
        text_widget.config(state='disabled')
        
        # Continue button
        continue_btn = tk.Button(
            intro_frame,
            text="🚀 START LEARNING JOURNEY",
            font=('Arial', 12, 'bold'),
            bg=self.colors['accent'],
            fg='white',
            command=self.show_attack_vectors,
            relief='raised',
            bd=3,
            padx=20,
            pady=10
        )
        continue_btn.pack(pady=20)
    
    def show_attack_vectors(self):
        self.clear_main_frame()
        self.current_phase = 1
        
        vectors_frame = tk.Frame(self.main_frame, bg=self.colors['background'])
        vectors_frame.pack(fill='both', expand=True, padx=20, pady=20)
        
        title = tk.Label(
            vectors_frame,
            text="📧 COMMON RANSOMWARE ATTACK VECTORS",
            font=('Arial', 16, 'bold'),
            bg=self.colors['background'],
            fg=self.colors['secondary']
        )
        title.pack(pady=10)
        
        vectors_info = """
🎯 HOW RANSOMWARE SPREADS:

1. 📧 EMAIL PHISHING (90% of attacks)
   • Malicious attachments (PDF, Word, Excel)
   • Fake invoices, shipping notifications
   • Urgent messages creating panic
   
2. 🌐 MALICIOUS WEBSITES
   • Drive-by downloads
   • Fake software updates
   • Compromised legitimate sites
   
3. 💾 REMOVABLE MEDIA
   • Infected USB drives
   • External hard drives
   • CD/DVD media
   
4. 🔗 NETWORK VULNERABILITIES
   • Unpatched systems
   • Weak passwords
   • Remote Desktop Protocol (RDP) attacks
   
5. 📱 SOCIAL ENGINEERING
   • Fake phone calls
   • Impersonation
   • Creating false urgency

⚡ REAL SCENARIO SIMULATION:
Let's simulate a typical phishing email that could deliver ransomware...
        """
        
        info_text = scrolledtext.ScrolledText(
            vectors_frame,
            wrap=tk.WORD,
            width=80,
            height=15,
            font=('Arial', 11),
            bg='white',
            fg=self.colors['text']
        )
        info_text.pack(pady=10, fill='both', expand=True)
        info_text.insert('1.0', vectors_info)
        info_text.config(state='disabled')
        
        next_btn = tk.Button(
            vectors_frame,
            text="📧 SIMULATE PHISHING EMAIL",
            font=('Arial', 12, 'bold'),
            bg=self.colors['warning'],
            fg='white',
            command=self.simulate_phishing_email,
            relief='raised',
            bd=3,
            padx=20,
            pady=10
        )
        next_btn.pack(pady=10)
    
    def simulate_phishing_email(self):
        self.clear_main_frame()
        
        email_frame = tk.Frame(self.main_frame, bg=self.colors['background'])
        email_frame.pack(fill='both', expand=True, padx=20, pady=20)
        
        title = tk.Label(
            email_frame,
            text="📧 PHISHING EMAIL SIMULATION",
            font=('Arial', 16, 'bold'),
            bg=self.colors['background'],
            fg=self.colors['warning']
        )
        title.pack(pady=10)
        
        # Create fake email interface
        email_container = tk.Frame(email_frame, bg='white', relief='ridge', bd=2)
        email_container.pack(fill='both', expand=True, pady=10)
        
        # Email header
        header_frame = tk.Frame(email_container, bg='#F0F0F0')
        header_frame.pack(fill='x', padx=5, pady=5)
        
        tk.Label(header_frame, text="From: billing@urgent-invoice.com", 
                font=('Arial', 10), bg='#F0F0F0').pack(anchor='w')
        tk.Label(header_frame, text="To: you@yourcompany.com", 
                font=('Arial', 10), bg='#F0F0F0').pack(anchor='w')
        tk.Label(header_frame, text="Subject: ⚠️ URGENT: Outstanding Invoice - Action Required", 
                font=('Arial', 10, 'bold'), bg='#F0F0F0', fg='red').pack(anchor='w')
        
        # Email body
        email_body = """
Dear Valued Customer,

Our records indicate you have an OVERDUE INVOICE of $2,847.50 that requires immediate attention.

ACCOUNT SUSPENSION will occur in 24 hours if payment is not processed immediately.

To avoid service interruption and additional fees, please:
1. Download and review the attached invoice (Invoice_#47281.pdf)
2. Process payment through our secure portal
3. Reply to confirm receipt

⚠️ WARNING: Failure to respond within 24 hours will result in:
• Account suspension
• Legal action
• Additional penalty fees of $500

Best regards,
Billing Department
Urgent Invoice Solutions
        """
        
        body_text = tk.Text(
            email_container,
            wrap=tk.WORD,
            height=12,
            font=('Arial', 11),
            bg='white'
        )
        body_text.pack(fill='both', expand=True, padx=10, pady=5)
        body_text.insert('1.0', email_body)
        body_text.config(state='disabled')
        
        # Attachment simulation
        attachment_frame = tk.Frame(email_container, bg='#FFE6E6')
        attachment_frame.pack(fill='x', padx=10, pady=5)
        
        tk.Label(attachment_frame, text="📎 Attachment: Invoice_#47281.pdf (WARNING: MALICIOUS)", 
                font=('Arial', 10, 'bold'), bg='#FFE6E6', fg='red').pack(anchor='w')
        
        # User choice buttons
        choice_frame = tk.Frame(email_frame, bg=self.colors['background'])
        choice_frame.pack(pady=20)
        
        tk.Label(choice_frame, text="What would you do?", 
                font=('Arial', 12, 'bold'), bg=self.colors['background']).pack(pady=5)
        
        btn_frame = tk.Frame(choice_frame, bg=self.colors['background'])
        btn_frame.pack()
        
        tk.Button(btn_frame, text="📎 Open Attachment", 
                 bg='#FF6B6B', fg='white', font=('Arial', 10),
                 command=lambda: self.handle_email_choice('open')).pack(side='left', padx=5)
        
        tk.Button(btn_frame, text="📧 Reply Immediately", 
                 bg='#FF9F43', fg='white', font=('Arial', 10),
                 command=lambda: self.handle_email_choice('reply')).pack(side='left', padx=5)
        
        tk.Button(btn_frame, text="🗑️ Delete Email", 
                 bg='#2ECC71', fg='white', font=('Arial', 10),
                 command=lambda: self.handle_email_choice('delete')).pack(side='left', padx=5)
        
        tk.Button(btn_frame, text="🔍 Investigate Further", 
                 bg='#3498DB', fg='white', font=('Arial', 10),
                 command=lambda: self.handle_email_choice('investigate')).pack(side='left', padx=5)
    
    def handle_email_choice(self, choice):
        if choice == 'open':
            self.knowledge_score += 10
            messagebox.showwarning("⚠️ INFECTED!", 
                                 "You opened a malicious attachment!\n\n"
                                 "In reality, this would have installed ransomware.\n"
                                 "LESSON: Never open unexpected attachments!")
            self.simulate_infection()
        elif choice == 'reply':
            self.knowledge_score += 20
            messagebox.showwarning("📧 Email Sent", 
                                 "You replied to the phishing email!\n\n"
                                 "This confirms your email is active.\n"
                                 "LESSON: Don't engage with suspicious emails!")
            self.show_red_flags()
        elif choice == 'delete':
            self.knowledge_score += 40
            messagebox.showinfo("✅ Good Choice!", 
                               "You deleted the suspicious email!\n\n"
                               "This was the right approach for obvious phishing.\n"
                               "LESSON: When in doubt, delete!")
            self.show_red_flags()
        elif choice == 'investigate':
            self.knowledge_score += 50
            messagebox.showinfo("🏆 Excellent!", 
                               "You chose to investigate first!\n\n"
                               "This is the BEST approach.\n"
                               "LESSON: Always verify before acting!")
            self.show_red_flags()
    
    def show_red_flags(self):
        self.clear_main_frame()
        
        flags_frame = tk.Frame(self.main_frame, bg=self.colors['background'])
        flags_frame.pack(fill='both', expand=True, padx=20, pady=20)
        
        title = tk.Label(
            flags_frame,
            text="🚩 RED FLAGS IN PHISHING EMAILS",
            font=('Arial', 16, 'bold'),
            bg=self.colors['background'],
            fg=self.colors['warning']
        )
        title.pack(pady=10)
        
        red_flags_text = """
🔍 WHAT TO LOOK FOR:

🚩 SENDER RED FLAGS:
   • Unknown or suspicious email addresses
   • Misspelled company names
   • Generic greetings ("Dear Customer")
   • Email doesn't match claimed organization

🚩 CONTENT RED FLAGS:
   • Creates false urgency ("24 hours", "immediate action")
   • Threatens consequences (suspension, legal action)
   • Requests personal information
   • Poor grammar and spelling
   • Generic, non-specific information

🚩 TECHNICAL RED FLAGS:
   • Unexpected attachments
   • Suspicious links (hover to preview)
   • Requests to download software
   • Asks to disable security features

🚩 BEHAVIORAL RED FLAGS:
   • Asks you to act quickly without thinking
   • Requests payment via unusual methods
   • Claims to be from a service you don't use
   • Too good to be true offers

✅ VERIFICATION STEPS:
1. Check sender's email address carefully
2. Contact organization through official channels
3. Don't click links - type URLs manually
4. Verify any claims independently
5. When in doubt, ask IT or security team

🎯 REMEMBER: Legitimate companies never ask for sensitive information via email!
        """
        
        text_widget = scrolledtext.ScrolledText(
            flags_frame,
            wrap=tk.WORD,
            width=80,
            height=18,
            font=('Arial', 11),
            bg='white',
            fg=self.colors['text']
        )
        text_widget.pack(pady=10, fill='both', expand=True)
        text_widget.insert('1.0', red_flags_text)
        text_widget.config(state='disabled')
        
        next_btn = tk.Button(
            flags_frame,
            text="⚠️ SIMULATE RANSOMWARE INFECTION",
            font=('Arial', 12, 'bold'),
            bg=self.colors['warning'],
            fg='white',
            command=self.simulate_infection,
            relief='raised',
            bd=3,
            padx=20,
            pady=10
        )
        next_btn.pack(pady=10)
    
    def simulate_infection(self):
        self.clear_main_frame()
        self.current_phase = 2
        
        infection_frame = tk.Frame(self.main_frame, bg='#2C3E50')
        infection_frame.pack(fill='both', expand=True)
        
        # Fake ransomware screen (educational simulation)
        warning_label = tk.Label(
            infection_frame,
            text="⚠️ EDUCATIONAL SIMULATION - NO REAL HARM ⚠️",
            font=('Arial', 14, 'bold'),
            bg='#E74C3C',
            fg='white'
        )
        warning_label.pack(fill='x', pady=5)
        
        skull_label = tk.Label(
            infection_frame,
            text="💀 YOUR FILES HAVE BEEN ENCRYPTED 💀",
            font=('Arial', 24, 'bold'),
            bg='#2C3E50',
            fg='#E74C3C'
        )
        skull_label.pack(pady=20)
        
        ransom_text = """
🔒 WHAT HAPPENED TO YOUR COMPUTER?

Your important files, documents, photos, databases and other files are encrypted with
strongest encryption and unique key, generated for this computer.

Private decryption key is stored on a secret internet server and nobody can decrypt your
files until you pay and obtain the private key.

💰 HOW TO RECOVER YOUR FILES?

You can purchase private decryption key. Price is $500 in Bitcoin.

1. Download Bitcoin wallet
2. Purchase $500 worth of Bitcoin  
3. Send Bitcoin to: 1A2B3C4D5E6F7G8H9I0J1K2L3M4N5O6P
4. Send proof of payment to: decrypt@evil-hackers.com
5. We will send you decryption software

⏰ TIME LIMIT: 72 HOURS

After 72 hours, decryption key will be deleted forever and your files will be lost forever.

❌ DO NOT:
• Turn off computer
• Delete files
• Contact police or FBI
• Use antivirus software
        """
        
        ransom_display = tk.Text(
            infection_frame,
            wrap=tk.WORD,
            font=('Courier', 12),
            bg='#2C3E50',
            fg='#E74C3C',
            height=20
        )
        ransom_display.pack(fill='both', expand=True, padx=20, pady=10)
        ransom_display.insert('1.0', ransom_text)
        ransom_display.config(state='disabled')
        
        # Progress bar showing "encryption"
        progress_frame = tk.Frame(infection_frame, bg='#2C3E50')
        progress_frame.pack(pady=10)
        
        tk.Label(progress_frame, text="Encrypting files...", 
                bg='#2C3E50', fg='white', font=('Arial', 12)).pack()
        
        self.progress = ttk.Progressbar(progress_frame, length=400, mode='determinate')
        self.progress.pack(pady=5)
        
        # Start fake encryption progress
        self.start_fake_encryption()
        
        # Continue button (appears after "encryption")
        self.continue_btn = tk.Button(
            infection_frame,
            text="📚 LEARN ABOUT IMPACT & RECOVERY",
            font=('Arial', 12, 'bold'),
            bg=self.colors['accent'],
            fg='white',
            command=self.show_impact_analysis,
            relief='raised',
            bd=3,
            padx=20,
            pady=10
        )
    
    def start_fake_encryption(self):
        def update_progress():
            for i in range(101):
                self.progress['value'] = i
                self.root.update_idletasks()
                time.sleep(0.05)
            
            self.continue_btn.pack(pady=20)
        
        thread = threading.Thread(target=update_progress)
        thread.daemon = True
        thread.start()
    
    def show_impact_analysis(self):
        self.clear_main_frame()
        self.current_phase = 3
        
        impact_frame = tk.Frame(self.main_frame, bg=self.colors['background'])
        impact_frame.pack(fill='both', expand=True, padx=20, pady=20)
        
        title = tk.Label(
            impact_frame,
            text="📊 RANSOMWARE IMPACT ANALYSIS",
            font=('Arial', 16, 'bold'),
            bg=self.colors['background'],
            fg=self.colors['secondary']
        )
        title.pack(pady=10)
        
        impact_text = """
💥 REAL-WORLD IMPACT OF RANSOMWARE ATTACKS:

🏢 BUSINESS IMPACT:
• Average downtime: 22 days
• Average cost: $4.54 million per incident
• 60% of small businesses close within 6 months after an attack
• Lost productivity, revenue, and customer trust
• Legal and regulatory consequences

🏥 HEALTHCARE IMPACT:
• Patient care disruption
• Delayed surgeries and treatments
• Medical device failures
• Potential loss of life in critical situations
• HIPAA violations and fines

🏛️ GOVERNMENT IMPACT:
• Public service disruption
• Citizen data exposure
• Emergency services affected
• Infrastructure vulnerabilities exposed
• National security concerns

👤 PERSONAL IMPACT:
• Lost family photos and memories
• Identity theft risks
• Financial losses
• Emotional distress and anxiety
• Time lost recovering data

💰 FINANCIAL BREAKDOWN:
• Ransom payment: $812,380 (average)
• Downtime costs: $1,448,458
• People costs: $1,213,383
• Device costs: $216,054
• Network costs: $198,682
• Lost opportunity: $1,163,896

🎯 KEY LESSON: Prevention is always cheaper than cure!
        """
        
        text_widget = scrolledtext.ScrolledText(
            impact_frame,
            wrap=tk.WORD,
            width=80,
            height=18,
            font=('Arial', 11),
            bg='white',
            fg=self.colors['text']
        )
        text_widget.pack(pady=10, fill='both', expand=True)
        text_widget.insert('1.0', impact_text)
        text_widget.config(state='disabled')
        
        next_btn = tk.Button(
            impact_frame,
            text="🛡️ LEARN PREVENTION STRATEGIES",
            font=('Arial', 12, 'bold'),
            bg=self.colors['safe'],
            fg='white',
            command=self.show_prevention_strategies,
            relief='raised',
            bd=3,
            padx=20,
            pady=10
        )
        next_btn.pack(pady=10)
    
    def show_prevention_strategies(self):
        self.clear_main_frame()
        self.current_phase = 4
        
        prevention_frame = tk.Frame(self.main_frame, bg=self.colors['background'])
        prevention_frame.pack(fill='both', expand=True, padx=20, pady=20)
        
        title = tk.Label(
            prevention_frame,
            text="🛡️ RANSOMWARE PREVENTION STRATEGIES",
            font=('Arial', 16, 'bold'),
            bg=self.colors['background'],
            fg=self.colors['safe']
        )
        title.pack(pady=10)
        
        prevention_text = """
🔐 COMPREHENSIVE PROTECTION STRATEGY:

1️⃣ BACKUP STRATEGY (3-2-1 Rule):
   ✅ 3 copies of important data
   ✅ 2 different storage media types
   ✅ 1 copy stored offsite/offline
   • Automated daily backups
   • Regular backup testing
   • Air-gapped backups (disconnected from network)

2️⃣ SOFTWARE SECURITY:
   ✅ Keep operating system updated
   ✅ Install security patches immediately
   ✅ Use reputable antivirus software
   ✅ Enable automatic updates
   ✅ Regular security scans

3️⃣ EMAIL SECURITY:
   ✅ Advanced email filtering
   ✅ Employee training programs
   ✅ Disable macros in Office documents
   ✅ Sandbox suspicious attachments
   ✅ Multi-factor authentication

4️⃣ NETWORK SECURITY:
   ✅ Firewall configuration
   ✅ Network segmentation
   ✅ VPN for remote access
   ✅ Disable unnecessary services
   ✅ Monitor network traffic

5️⃣ ACCESS CONTROL:
   ✅ Principle of least privilege
   ✅ Strong password policies
   ✅ Multi-factor authentication (MFA)
   ✅ Regular access reviews
   ✅ Privileged account management

6️⃣ EMPLOYEE TRAINING:
   ✅ Regular phishing simulations
   ✅ Security awareness programs
   ✅ Incident reporting procedures
   ✅ Social engineering awareness
   ✅ Clean desk policies

7️⃣ INCIDENT RESPONSE PLAN:
   ✅ Written response procedures
   ✅ Emergency contact list
   ✅ Communication plan
   ✅ Recovery priorities
   ✅ Regular plan testing

💡 REMEMBER: Layered security is key - no single solution is perfect!
        """
        
        text_widget = scrolledtext.ScrolledText(
            prevention_frame,
            wrap=tk.WORD,
            width=80,
            height=20,
            font=('Arial', 11),
            bg='white',
            fg=self.colors['text']
        )
        text_widget.pack(pady=10, fill='both', expand=True)
        text_widget.insert('1.0', prevention_text)
        text_widget.config(state='disabled')
        
        next_btn = tk.Button(
            prevention_frame,
            text="🚨 LEARN RESPONSE PROCEDURES",
            font=('Arial', 12, 'bold'),
            bg=self.colors['warning'],
            fg='white',
            command=self.show_response_procedures,
            relief='raised',
            bd=3,
            padx=20,
            pady=10
        )
        next_btn.pack(pady=10)
    
    def show_response_procedures(self):
        self.clear_main_frame()
        self.current_phase = 5
        
        response_frame = tk.Frame(self.main_frame, bg=self.colors['background'])
        response_frame.pack(fill='both', expand=True, padx=20, pady=20)
        
        title = tk.Label(
            response_frame,
            text="🚨 RANSOMWARE INCIDENT RESPONSE",
            font=('Arial', 16, 'bold'),
            bg=self.colors['background'],
            fg=self.colors['warning']
        )
        title.pack(pady=10)
        
        response_text = """
⚡ IMMEDIATE RESPONSE STEPS (First 30 minutes):

🔴 STEP 1: ISOLATE THE INFECTION
   1. Disconnect infected device from network immediately
   2. Do NOT shut down the computer (may lose encryption keys)
   3. Isolate affected network segments
   4. Disable wireless connections
   5. Document everything you observe

🔴 STEP 2: ASSESS THE SCOPE  
   1. Identify all affected systems
   2. Check for lateral movement
   3. Verify backup integrity
   4. Document file types affected
   5. Take screenshots for evidence

🔴 STEP 3: ACTIVATE INCIDENT RESPONSE TEAM
   1. Notify IT security team
   2. Contact management
   3. Inform legal department
   4. Engage cybersecurity experts
   5. Consider law enforcement contact

🔴 STEP 4: PRESERVE EVIDENCE
   1. Create forensic images if possible
   2. Document all actions taken
   3. Preserve system logs
   4. Save ransom notes
   5. Photograph affected screens

📞 WHO TO CONTACT:
   • Internal IT/Security team (FIRST)
   • Law enforcement (FBI, local police)
   • Cyber insurance provider
   • Legal counsel
   • Cybersecurity incident response firm
   • Public relations (if needed)

❌ WHAT NOT TO DO:
   • Don't pay the ransom (funds criminals, no guarantee)
   • Don't try to decrypt files yourself
   • Don't restart systems unnecessarily  
   • Don't communicate via compromised systems
   • Don't delay reporting to authorities

🔄 RECOVERY PRIORITIES:
   1. Critical business operations
   2. Customer-facing systems
   3. Financial systems
   4. Communication systems
   5. Supporting infrastructure

⚖️ LEGAL CONSIDERATIONS:
   • Data breach notification laws
   • Industry compliance requirements
   • Insurance claim procedures
   • Evidence preservation
   • Public disclosure requirements
        """
        
        text_widget = scrolledtext.ScrolledText(
            response_frame,
            wrap=tk.WORD,
            width=80,
            height=20,
            font=('Arial', 11),
            bg='white',
            fg=self.colors['text']
        )
        text_widget.pack(pady=10, fill='both', expand=True)
        text_widget.insert('1.0', response_text)
        text_widget.config(state='disabled')
        
        next_btn = tk.Button(
            response_frame,
            text="🎓 TAKE KNOWLEDGE QUIZ",
            font=('Arial', 12, 'bold'),
            bg=self.colors['primary'],
            fg='white',
            command=self.start_quiz,
            relief='raised',
            bd=3,
            padx=20,
            pady=10
        )
        next_btn.pack(pady=10)
    
    def start_quiz(self):
        self.clear_main_frame()
        self.quiz_score = 0
        self.quiz_questions = [
            {
                "question": "What percentage of ransomware attacks come through email phishing?",
                "options": ["50%", "70%", "90%", "95%"],
                "correct": 2,
                "explanation": "90% of ransomware attacks originate from phishing emails, making email security crucial."
            },
            {
                "question": "What is the 3-2-1 backup rule?",
                "options": [
                    "3 backups, 2 locations, 1 test per month",
                    "3 copies of data, 2 different media, 1 offsite",
                    "3 passwords, 2 factors, 1 admin",
                    "3 antivirus, 2 firewalls, 1 VPN"
                ],
                "correct": 1,
                "explanation": "3-2-1 rule: 3 copies of data, 2 different storage media, 1 copy stored offsite."
            },
            {
                "question": "What should you do FIRST if you suspect ransomware?",
                "options": [
                    "Pay the ransom immediately",
                    "Restart the computer",
                    "Disconnect from network",
                    "Delete all files"
                ],
                "correct": 2,
                "explanation": "Immediately disconnect from the network to prevent spread to other systems."
            },
            {
                "question": "What is the average cost of a ransomware attack?",
                "options": ["$1.2 million", "$4.54 million", "$500,000", "$10 million"],
                "correct": 1,
                "explanation": "The average cost of a ransomware attack is $4.54 million including downtime and recovery."
            },
            {
                "question": "Should you pay the ransom?",
                "options": [
                    "Yes, always pay immediately",
                    "Only if files are very important",
                    "No, it funds criminals and doesn't guarantee recovery",
                    "Only if amount is small"
                ],
                "correct": 2,
                "explanation": "Never pay ransoms - it funds criminal activities and there's no guarantee of file recovery."
            }
        ]
        self.current_question = 0
        self.show_quiz_question()
    
    def show_quiz_question(self):
        self.clear_main_frame()
        
        quiz_frame = tk.Frame(self.main_frame, bg=self.colors['background'])
        quiz_frame.pack(fill='both', expand=True, padx=20, pady=20)
        
        # Quiz header
        header = tk.Label(
            quiz_frame,
            text=f"🎓 KNOWLEDGE QUIZ - Question {self.current_question + 1}/{len(self.quiz_questions)}",
            font=('Arial', 16, 'bold'),
            bg=self.colors['background'],
            fg=self.colors['primary']
        )
        header.pack(pady=10)
        
        # Progress bar
        progress = ttk.Progressbar(
            quiz_frame, 
            length=400, 
            mode='determinate',
            value=(self.current_question / len(self.quiz_questions)) * 100
        )
        progress.pack(pady=10)
        
        # Question
        question_frame = tk.Frame(quiz_frame, bg='white', relief='ridge', bd=2)
        question_frame.pack(fill='x', pady=20, padx=20)
        
        question_text = tk.Label(
            question_frame,
            text=self.quiz_questions[self.current_question]["question"],
            font=('Arial', 14, 'bold'),
            bg='white',
            fg=self.colors['text'],
            wraplength=600,
            pady=20
        )
        question_text.pack()
        
        # Options
        self.quiz_var = tk.StringVar()
        options_frame = tk.Frame(quiz_frame, bg=self.colors['background'])
        options_frame.pack(pady=20)
        
        for i, option in enumerate(self.quiz_questions[self.current_question]["options"]):
            rb = tk.Radiobutton(
                options_frame,
                text=f"{chr(65+i)}. {option}",
                variable=self.quiz_var,
                value=str(i),
                font=('Arial', 12),
                bg=self.colors['background'],
                fg=self.colors['text'],
                selectcolor='white',
                pady=10
            )
            rb.pack(anchor='w', padx=20)
        
        # Submit button
        submit_btn = tk.Button(
            quiz_frame,
            text="✅ SUBMIT ANSWER",
            font=('Arial', 12, 'bold'),
            bg=self.colors['accent'],
            fg='white',
            command=self.check_answer,
            relief='raised',
            bd=3,
            padx=20,
            pady=10
        )
        submit_btn.pack(pady=20)
    
    def check_answer(self):
        if not self.quiz_var.get():
            messagebox.showwarning("No Selection", "Please select an answer before submitting.")
            return
        
        selected = int(self.quiz_var.get())
        correct = self.quiz_questions[self.current_question]["correct"]
        explanation = self.quiz_questions[self.current_question]["explanation"]
        
        if selected == correct:
            self.quiz_score += 1
            messagebox.showinfo("✅ Correct!", f"Well done!\n\n{explanation}")
        else:
            correct_answer = self.quiz_questions[self.current_question]["options"][correct]
            messagebox.showinfo("❌ Incorrect", f"The correct answer is: {correct_answer}\n\n{explanation}")
        
        self.current_question += 1
        
        if self.current_question < len(self.quiz_questions):
            self.show_quiz_question()
        else:
            self.show_quiz_results()
    
    def show_quiz_results(self):
        self.clear_main_frame()
        
        results_frame = tk.Frame(self.main_frame, bg=self.colors['background'])
        results_frame.pack(fill='both', expand=True, padx=20, pady=20)
        
        # Calculate final knowledge score
        quiz_percentage = (self.quiz_score / len(self.quiz_questions)) * 100
        final_score = min(70 + (quiz_percentage * 0.3), 100)  # Base 70% + quiz bonus
        
        title = tk.Label(
            results_frame,
            text="🎓 CONGRATULATIONS! COURSE COMPLETED",
            font=('Arial', 18, 'bold'),
            bg=self.colors['background'],
            fg=self.colors['safe']
        )
        title.pack(pady=20)
        
        # Score display
        score_frame = tk.Frame(results_frame, bg='white', relief='ridge', bd=3)
        score_frame.pack(pady=20, padx=50, fill='x')
        
        tk.Label(score_frame, text=f"📊 Your Quiz Score: {self.quiz_score}/{len(self.quiz_questions)} ({quiz_percentage:.0f}%)",
                font=('Arial', 14, 'bold'), bg='white', fg=self.colors['primary']).pack(pady=10)
        
        tk.Label(score_frame, text=f"🧠 Estimated Knowledge Level: {final_score:.0f}%",
                font=('Arial', 16, 'bold'), bg='white', fg=self.colors['safe']).pack(pady=10)
        
        # Knowledge summary
        summary_text = f"""
🎯 LEARNING JOURNEY COMPLETE!

From 0% to {final_score:.0f}% Knowledge - Outstanding Progress!

✅ WHAT YOU'VE LEARNED:
• Ransomware definition and attack vectors
• How to identify phishing emails and red flags
• Real-world impact and costs of attacks
• Comprehensive prevention strategies
• Proper incident response procedures
• Recovery and backup best practices

🛡️ YOU'RE NOW EQUIPPED TO:
• Recognize potential ransomware threats
• Implement effective security measures
• Respond appropriately to incidents
• Educate others about cybersecurity
• Make informed security decisions

🌟 NEXT STEPS:
• Share this knowledge with colleagues
• Implement security measures in your organization
• Stay updated on cybersecurity threats
• Consider additional security training
• Practice safe computing habits daily

🏆 REMEMBER: You are now part of the solution in fighting cybercrime!

Thank you for completing the Ransomware Education Simulator!
Stay safe and stay secure! 🔐
        """
        
        summary_widget = scrolledtext.ScrolledText(
            results_frame,
            wrap=tk.WORD,
            width=80,
            height=18,
            font=('Arial', 11),
            bg='white',
            fg=self.colors['text']
        )
        summary_widget.pack(pady=10, fill='both', expand=True)
        summary_widget.insert('1.0', summary_text)
        summary_widget.config(state='disabled')
        
        # Action buttons
        button_frame = tk.Frame(results_frame, bg=self.colors['background'])
        button_frame.pack(pady=20)
        
        tk.Button(button_frame, text="🔄 RESTART COURSE", 
                 font=('Arial', 12, 'bold'), bg=self.colors['primary'], fg='white',
                 command=self.restart_course, relief='raised', bd=3, padx=20, pady=10).pack(side='left', padx=10)
        
        tk.Button(button_frame, text="📚 ADDITIONAL RESOURCES", 
                 font=('Arial', 12, 'bold'), bg=self.colors['accent'], fg='white',
                 command=self.show_resources, relief='raised', bd=3, padx=20, pady=10).pack(side='left', padx=10)
        
        tk.Button(button_frame, text="❌ EXIT", 
                 font=('Arial', 12, 'bold'), bg=self.colors['secondary'], fg='white',
                 command=self.root.quit, relief='raised', bd=3, padx=20, pady=10).pack(side='left', padx=10)
    
    def show_resources(self):
        self.clear_main_frame()
        
        resources_frame = tk.Frame(self.main_frame, bg=self.colors['background'])
        resources_frame.pack(fill='both', expand=True, padx=20, pady=20)
        
        title = tk.Label(
            resources_frame,
            text="📚 ADDITIONAL CYBERSECURITY RESOURCES",
            font=('Arial', 16, 'bold'),
            bg=self.colors['background'],
            fg=self.colors['primary']
        )
        title.pack(pady=10)
        
        resources_text = """
🔗 OFFICIAL RESOURCES:

🏛️ GOVERNMENT AGENCIES:
• CISA (Cybersecurity & Infrastructure Security Agency)
  - StopRansomware.gov
  - Free cybersecurity tools and guides
• FBI Internet Crime Complaint Center (IC3)
• NIST Cybersecurity Framework

🛡️ CYBERSECURITY ORGANIZATIONS:
• SANS Institute - Training and certifications
• (ISC)² - Information security certifications
• ISACA - IT governance and risk management
• CompTIA - Entry-level cybersecurity certifications

📖 EDUCATIONAL RESOURCES:
• Cybrary - Free cybersecurity training
• Coursera - University cybersecurity courses
• edX - MIT and Harvard security courses
• OWASP - Web application security

🔧 FREE SECURITY TOOLS:
• Malwarebytes - Anti-malware protection
• Windows Defender - Built-in antivirus
• Wireshark - Network analysis tool
• Nmap - Network security scanner

📱 SECURITY AWARENESS:
• KnowBe4 - Phishing simulation training
• Proofpoint - Security awareness platform
• SANS Securing the Human - Awareness training

📊 THREAT INTELLIGENCE:
• US-CERT Alerts and Advisories
• CVE Database - Vulnerability information
• MITRE ATT&CK Framework
• Krebs on Security - Security news blog

💼 BUSINESS RESOURCES:
• Cyber Insurance providers
• Incident response companies
• Managed security service providers (MSSPs)
• Business continuity planning resources

🎯 STAY INFORMED:
• Subscribe to security newsletters
• Follow cybersecurity experts on social media
• Attend local cybersecurity meetups
• Participate in online security communities

Remember: Cybersecurity is an ongoing journey, not a destination!
        """
        
        text_widget = scrolledtext.ScrolledText(
            resources_frame,
            wrap=tk.WORD,
            width=80,
            height=20,
            font=('Arial', 11),
            bg='white',
            fg=self.colors['text']
        )
        text_widget.pack(pady=10, fill='both', expand=True)
        text_widget.insert('1.0', resources_text)
        text_widget.config(state='disabled')
        
        back_btn = tk.Button(
            resources_frame,
            text="⬅️ BACK TO RESULTS",
            font=('Arial', 12, 'bold'),
            bg=self.colors['primary'],
            fg='white',
            command=self.show_quiz_results,
            relief='raised',
            bd=3,
            padx=20,
            pady=10
        )
        back_btn.pack(pady=10)
    
    def restart_course(self):
        self.current_phase = 0
        self.knowledge_score = 0
        self.quiz_score = 0
        self.show_introduction()
    
    def clear_main_frame(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()
    
    def run(self):
        self.root.mainloop()

# Main execution
if __name__ == "__main__":
    print("🛡️ Starting Educational Ransomware Simulator...")
    print("⚠️  DISCLAIMER: This is a 100% safe educational tool.")
    print("📚 No real files will be harmed or encrypted.")
    print("🎯 Purpose: Learn about ransomware threats and protection.")
    print("-" * 60)
    
    try:
        app = RansomwareEducationSimulator()
        app.run()
    except KeyboardInterrupt:
        print("\n👋 Educational session ended by user.")
    except Exception as e:
        print(f"❌ Error occurred: {e}")
        print("Please ensure you have tkinter installed: pip install tkinter")
    
    print("Thank you for learning about cybersecurity! Stay safe! 🔐")