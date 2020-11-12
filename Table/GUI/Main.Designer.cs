namespace ATC_GUI
{
    partial class Main
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.Act_list = new System.Windows.Forms.ListBox();
            this.Settings = new System.Windows.Forms.GroupBox();
            this.label8 = new System.Windows.Forms.Label();
            this.Prereq_cmb = new System.Windows.Forms.ComboBox();
            this.Type_cmb = new System.Windows.Forms.ComboBox();
            this.Targets = new System.Windows.Forms.GroupBox();
            this.T_reset = new System.Windows.Forms.Button();
            this.T_list = new System.Windows.Forms.ListBox();
            this.label4 = new System.Windows.Forms.Label();
            this.T_add = new System.Windows.Forms.Button();
            this.label6 = new System.Windows.Forms.Label();
            this.T_grp_cmb = new System.Windows.Forms.ComboBox();
            this.label7 = new System.Windows.Forms.Label();
            this.T_maj_cmb = new System.Windows.Forms.ComboBox();
            this.T_crs_cmb = new System.Windows.Forms.ComboBox();
            this.label3 = new System.Windows.Forms.Label();
            this.label2 = new System.Windows.Forms.Label();
            this.Inst_txt = new System.Windows.Forms.TextBox();
            this.label1 = new System.Windows.Forms.Label();
            this.Name_txt = new System.Windows.Forms.TextBox();
            this.Add_btn = new System.Windows.Forms.Button();
            this.Gen_btn = new System.Windows.Forms.Button();
            this.Rem_btn = new System.Windows.Forms.Button();
            this.Upd_btn = new System.Windows.Forms.Button();
            this.label5 = new System.Windows.Forms.Label();
            this.Settings.SuspendLayout();
            this.Targets.SuspendLayout();
            this.SuspendLayout();
            // 
            // Act_list
            // 
            this.Act_list.FormattingEnabled = true;
            this.Act_list.Location = new System.Drawing.Point(12, 12);
            this.Act_list.Name = "Act_list";
            this.Act_list.Size = new System.Drawing.Size(231, 433);
            this.Act_list.TabIndex = 1;
            this.Act_list.SelectedIndexChanged += new System.EventHandler(this.Act_list_SelectedIndexChanged);
            this.Act_list.MouseDown += new System.Windows.Forms.MouseEventHandler(this.Act_list_Deselect);
            // 
            // Settings
            // 
            this.Settings.Controls.Add(this.label8);
            this.Settings.Controls.Add(this.Prereq_cmb);
            this.Settings.Controls.Add(this.Type_cmb);
            this.Settings.Controls.Add(this.Targets);
            this.Settings.Controls.Add(this.label3);
            this.Settings.Controls.Add(this.label2);
            this.Settings.Controls.Add(this.Inst_txt);
            this.Settings.Controls.Add(this.label1);
            this.Settings.Controls.Add(this.Name_txt);
            this.Settings.Location = new System.Drawing.Point(260, 12);
            this.Settings.Name = "Settings";
            this.Settings.Size = new System.Drawing.Size(373, 334);
            this.Settings.TabIndex = 2;
            this.Settings.TabStop = false;
            this.Settings.Text = "New activity (id = 0)";
            // 
            // label8
            // 
            this.label8.AutoSize = true;
            this.label8.Location = new System.Drawing.Point(24, 137);
            this.label8.Name = "label8";
            this.label8.Size = new System.Drawing.Size(62, 13);
            this.label8.TabIndex = 19;
            this.label8.Text = "Prerequisite";
            // 
            // Prereq_cmb
            // 
            this.Prereq_cmb.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
            this.Prereq_cmb.FormattingEnabled = true;
            this.Prereq_cmb.Items.AddRange(new object[] {
            "None"});
            this.Prereq_cmb.Location = new System.Drawing.Point(94, 134);
            this.Prereq_cmb.Name = "Prereq_cmb";
            this.Prereq_cmb.Size = new System.Drawing.Size(265, 21);
            this.Prereq_cmb.TabIndex = 18;
            this.Prereq_cmb.Click += new System.EventHandler(this.Prereq_cmb_Click);
            // 
            // Type_cmb
            // 
            this.Type_cmb.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
            this.Type_cmb.FormattingEnabled = true;
            this.Type_cmb.Items.AddRange(new object[] {
            "Lecture",
            "Tutorial",
            "Lab"});
            this.Type_cmb.Location = new System.Drawing.Point(94, 97);
            this.Type_cmb.Name = "Type_cmb";
            this.Type_cmb.Size = new System.Drawing.Size(78, 21);
            this.Type_cmb.TabIndex = 10;
            // 
            // Targets
            // 
            this.Targets.Controls.Add(this.T_reset);
            this.Targets.Controls.Add(this.T_list);
            this.Targets.Controls.Add(this.label4);
            this.Targets.Controls.Add(this.T_add);
            this.Targets.Controls.Add(this.label6);
            this.Targets.Controls.Add(this.T_grp_cmb);
            this.Targets.Controls.Add(this.label7);
            this.Targets.Controls.Add(this.T_maj_cmb);
            this.Targets.Controls.Add(this.T_crs_cmb);
            this.Targets.Location = new System.Drawing.Point(27, 174);
            this.Targets.Name = "Targets";
            this.Targets.Size = new System.Drawing.Size(332, 144);
            this.Targets.TabIndex = 16;
            this.Targets.TabStop = false;
            this.Targets.Text = "Targets";
            // 
            // T_reset
            // 
            this.T_reset.Location = new System.Drawing.Point(110, 109);
            this.T_reset.Name = "T_reset";
            this.T_reset.Size = new System.Drawing.Size(75, 23);
            this.T_reset.TabIndex = 18;
            this.T_reset.Text = "Reset";
            this.T_reset.UseVisualStyleBackColor = true;
            this.T_reset.Click += new System.EventHandler(this.T_reset_Click);
            // 
            // T_list
            // 
            this.T_list.FormattingEnabled = true;
            this.T_list.Location = new System.Drawing.Point(206, 15);
            this.T_list.Name = "T_list";
            this.T_list.Size = new System.Drawing.Size(110, 108);
            this.T_list.TabIndex = 7;
            // 
            // label4
            // 
            this.label4.AutoSize = true;
            this.label4.Location = new System.Drawing.Point(21, 22);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(40, 13);
            this.label4.TabIndex = 7;
            this.label4.Text = "Course";
            // 
            // T_add
            // 
            this.T_add.Location = new System.Drawing.Point(24, 109);
            this.T_add.Name = "T_add";
            this.T_add.Size = new System.Drawing.Size(75, 23);
            this.T_add.TabIndex = 17;
            this.T_add.Text = "Add";
            this.T_add.UseVisualStyleBackColor = true;
            this.T_add.Click += new System.EventHandler(this.T_add_Click);
            // 
            // label6
            // 
            this.label6.AutoSize = true;
            this.label6.Location = new System.Drawing.Point(21, 49);
            this.label6.Name = "label6";
            this.label6.Size = new System.Drawing.Size(33, 13);
            this.label6.TabIndex = 11;
            this.label6.Text = "Major";
            // 
            // T_grp_cmb
            // 
            this.T_grp_cmb.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
            this.T_grp_cmb.FormattingEnabled = true;
            this.T_grp_cmb.Items.AddRange(new object[] {
            "All"});
            this.T_grp_cmb.Location = new System.Drawing.Point(110, 73);
            this.T_grp_cmb.Name = "T_grp_cmb";
            this.T_grp_cmb.Size = new System.Drawing.Size(78, 21);
            this.T_grp_cmb.TabIndex = 15;
            this.T_grp_cmb.Click += new System.EventHandler(this.T_grp_cmb_Click);
            // 
            // label7
            // 
            this.label7.AutoSize = true;
            this.label7.Location = new System.Drawing.Point(21, 76);
            this.label7.Name = "label7";
            this.label7.Size = new System.Drawing.Size(36, 13);
            this.label7.TabIndex = 12;
            this.label7.Text = "Group";
            // 
            // T_maj_cmb
            // 
            this.T_maj_cmb.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
            this.T_maj_cmb.FormattingEnabled = true;
            this.T_maj_cmb.Items.AddRange(new object[] {
            "All"});
            this.T_maj_cmb.Location = new System.Drawing.Point(110, 46);
            this.T_maj_cmb.Name = "T_maj_cmb";
            this.T_maj_cmb.Size = new System.Drawing.Size(78, 21);
            this.T_maj_cmb.TabIndex = 14;
            this.T_maj_cmb.Click += new System.EventHandler(this.T_maj_cmb_Click);
            // 
            // T_crs_cmb
            // 
            this.T_crs_cmb.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
            this.T_crs_cmb.FormattingEnabled = true;
            this.T_crs_cmb.Items.AddRange(new object[] {
            "All"});
            this.T_crs_cmb.Location = new System.Drawing.Point(110, 19);
            this.T_crs_cmb.Name = "T_crs_cmb";
            this.T_crs_cmb.Size = new System.Drawing.Size(78, 21);
            this.T_crs_cmb.TabIndex = 13;
            this.T_crs_cmb.Click += new System.EventHandler(this.T_crs_cmb_Click);
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(24, 100);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(31, 13);
            this.label3.TabIndex = 5;
            this.label3.Text = "Type";
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(24, 65);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(51, 13);
            this.label2.TabIndex = 3;
            this.label2.Text = "Instructor";
            // 
            // Inst_txt
            // 
            this.Inst_txt.Location = new System.Drawing.Point(94, 62);
            this.Inst_txt.Name = "Inst_txt";
            this.Inst_txt.Size = new System.Drawing.Size(265, 20);
            this.Inst_txt.TabIndex = 2;
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(24, 30);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(35, 13);
            this.label1.TabIndex = 1;
            this.label1.Text = "Name";
            // 
            // Name_txt
            // 
            this.Name_txt.Location = new System.Drawing.Point(94, 27);
            this.Name_txt.Name = "Name_txt";
            this.Name_txt.Size = new System.Drawing.Size(265, 20);
            this.Name_txt.TabIndex = 0;
            // 
            // Add_btn
            // 
            this.Add_btn.Location = new System.Drawing.Point(318, 365);
            this.Add_btn.Name = "Add_btn";
            this.Add_btn.Size = new System.Drawing.Size(127, 39);
            this.Add_btn.TabIndex = 3;
            this.Add_btn.Text = "Add activity as new";
            this.Add_btn.UseVisualStyleBackColor = true;
            this.Add_btn.Click += new System.EventHandler(this.Add_btn_Click);
            // 
            // Gen_btn
            // 
            this.Gen_btn.Location = new System.Drawing.Point(451, 410);
            this.Gen_btn.Name = "Gen_btn";
            this.Gen_btn.Size = new System.Drawing.Size(127, 39);
            this.Gen_btn.TabIndex = 4;
            this.Gen_btn.Text = "Generate Schedule";
            this.Gen_btn.UseVisualStyleBackColor = true;
            this.Gen_btn.Click += new System.EventHandler(this.Gen_btn_Click);
            // 
            // Rem_btn
            // 
            this.Rem_btn.Location = new System.Drawing.Point(318, 410);
            this.Rem_btn.Name = "Rem_btn";
            this.Rem_btn.Size = new System.Drawing.Size(127, 39);
            this.Rem_btn.TabIndex = 6;
            this.Rem_btn.Text = "Remove Selected";
            this.Rem_btn.UseVisualStyleBackColor = true;
            this.Rem_btn.Click += new System.EventHandler(this.Rem_btn_Click);
            // 
            // Upd_btn
            // 
            this.Upd_btn.Location = new System.Drawing.Point(451, 365);
            this.Upd_btn.Name = "Upd_btn";
            this.Upd_btn.Size = new System.Drawing.Size(127, 39);
            this.Upd_btn.TabIndex = 5;
            this.Upd_btn.Text = "Update Selected";
            this.Upd_btn.UseVisualStyleBackColor = true;
            this.Upd_btn.Click += new System.EventHandler(this.Upd_btn_Click);
            // 
            // label5
            // 
            this.label5.AutoSize = true;
            this.label5.Location = new System.Drawing.Point(12, 452);
            this.label5.Name = "label5";
            this.label5.Size = new System.Drawing.Size(150, 13);
            this.label5.TabIndex = 7;
            this.label5.Text = "Hint: Right click to deselect all";
            // 
            // Main
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(653, 474);
            this.Controls.Add(this.label5);
            this.Controls.Add(this.Rem_btn);
            this.Controls.Add(this.Upd_btn);
            this.Controls.Add(this.Gen_btn);
            this.Controls.Add(this.Add_btn);
            this.Controls.Add(this.Settings);
            this.Controls.Add(this.Act_list);
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.FixedSingle;
            this.MaximizeBox = false;
            this.Name = "Main";
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
            this.Text = "Automatic Timetable Creator";
            this.Load += new System.EventHandler(this.Main_Load);
            this.Settings.ResumeLayout(false);
            this.Settings.PerformLayout();
            this.Targets.ResumeLayout(false);
            this.Targets.PerformLayout();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.ListBox Act_list;
        private System.Windows.Forms.GroupBox Settings;
        private System.Windows.Forms.Button Add_btn;
        private System.Windows.Forms.Button Gen_btn;
        private System.Windows.Forms.Label label8;
        private System.Windows.Forms.ComboBox Prereq_cmb;
        private System.Windows.Forms.ComboBox Type_cmb;
        private System.Windows.Forms.GroupBox Targets;
        private System.Windows.Forms.ListBox T_list;
        private System.Windows.Forms.Label label4;
        private System.Windows.Forms.Button T_add;
        private System.Windows.Forms.Label label6;
        private System.Windows.Forms.ComboBox T_grp_cmb;
        private System.Windows.Forms.Label label7;
        private System.Windows.Forms.ComboBox T_maj_cmb;
        private System.Windows.Forms.ComboBox T_crs_cmb;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.TextBox Inst_txt;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.TextBox Name_txt;
        private System.Windows.Forms.Button Rem_btn;
        private System.Windows.Forms.Button Upd_btn;
        private System.Windows.Forms.Button T_reset;
        private System.Windows.Forms.Label label5;
    }
}

