using System;
using System.Windows.Forms;
using System.Collections.Generic;
using System.Diagnostics;

namespace ATC_GUI
{
    public partial class Main : Form
    {
        bool success, save_pending;

        // Serializing Settings GroupBox, the lazy-way.
        readonly List<(string, string, int, int, List<(string,string,string)>)> Box = 
            new List<(string, string, int, int, List<(string,string,string)>)>();
        List<string> Removed = new List<string>();
        public Main()
        {
            InitializeComponent();
        }

        private void Main_Load(object sender, EventArgs e)
        {
            SetComboBoxesDefaults();
        }

        private void SetComboBoxesDefaults()
        {
            // Sets comboboxes values in Settings to default values
            if (T_crs_cmb.SelectedIndex == -1) Type_cmb.SelectedIndex = 0;
            if (T_crs_cmb.SelectedIndex == -1) T_crs_cmb.SelectedIndex = 0;
            if (T_maj_cmb.SelectedIndex == -1) T_maj_cmb.SelectedIndex = 0;
            if (T_grp_cmb.SelectedIndex == -1) T_grp_cmb.SelectedIndex = 0;
            if (Prereq_cmb.SelectedIndex == -1) Prereq_cmb.SelectedIndex = 0;
            T_crs_cmb.SelectedIndex = 0;
            T_maj_cmb.SelectedIndex = 0;
            T_grp_cmb.SelectedIndex = 0;
        }

        void SettingsSave(int idx)
        {
            Debug.WriteLine("Saving...");
            List<(string,string,string)> tmp = new List<(string,string,string)>();
            foreach ((string,string,string) t in T_list.Items) tmp.Add(t);
            if (idx == -1)
            {
                Box.Add((Name_txt.Text, Inst_txt.Text, Type_cmb.SelectedIndex, Prereq_cmb.SelectedIndex, tmp));
            }
            else
            {
                Box[idx] = (Name_txt.Text, Inst_txt.Text, Type_cmb.SelectedIndex, Prereq_cmb.SelectedIndex, tmp);
            }
        }

        void SettingsLoad(int idx)
        {
            if (idx >= Box.Count || save_pending) return;
            Debug.WriteLine("Loading...");
            SetComboBoxesDefaults();
            Name_txt.Text = Box[idx].Item1;
            Inst_txt.Text = Box[idx].Item2;
            Type_cmb.SelectedIndex = Box[idx].Item3;
            if (Removed.Contains((string)Prereq_cmb.Items[Box[idx].Item4]))
            {
                MessageBox.Show("Referenced Activity no longer exists");
                Prereq_cmb.SelectedIndex = 0;
            }
            else Prereq_cmb.SelectedIndex = Box[idx].Item4;
            T_list.Items.Clear();
            foreach (var t in Box[idx].Item5)
                T_list.Items.Add(t);
        }

        private void Add_btn_Click(object sender, EventArgs e)
        {
            // Reset settings, add a new Activity, select it, then click update, on fail remove.
            Act_list.Items.Add("untitled");
            Act_list.SetSelected(Act_list.Items.Count - 1, true);

            success = false;
            Upd_btn_Click(sender, e);
            if (success == false)
                Act_list.Items.RemoveAt(Act_list.Items.Count - 1);

            if (Act_list.Items.Count != 0)
            {
                Name_txt.Text = string.Empty;
                Inst_txt.Text = string.Empty;
                T_list.Items.Clear();
                SetComboBoxesDefaults();
                Act_list.SetSelected(Act_list.Items.Count - 1, false);
            }
        }

        private void Rem_btn_Click(object sender, EventArgs e)
        {
            // Remove selected activity item
            int idx = Act_list.SelectedIndex;
            if (idx == -1)
            {
                MessageBox.Show("Nothing is selected");
                return;
            }
            Globals.data.RemoveAt(idx);
            Box.RemoveAt(idx);
            Removed.Add(idx + ": " + (string)Act_list.Items[idx]);
            Act_list.Items.RemoveAt(idx);
        }

        private void Upd_btn_Click(object sender, EventArgs e)
        {
            save_pending = true;

            // Validate and collect data in Settings
            int idx = Act_list.SelectedIndex;
            if (idx == -1)
            {
                MessageBox.Show("Nothing is selected");
                return;
            }

            if (Name_txt.Text == string.Empty)
            {
                MessageBox.Show("Activity Name cannot be empty");
                return;
            }
            if (Inst_txt.Text == string.Empty)
            {
                MessageBox.Show("Activity Instructor Name cannot be empty");
                return;
            }
            if (Type_cmb.SelectedIndex == -1)
            {
                MessageBox.Show("Activity should have a type");
                return;
            }
            if (T_list.Items.Count == 0)
            {
                MessageBox.Show("Activity should have at least one target");
                return;
            }

            Act_list.Items[idx] = Name_txt.Text + " - " + Type_cmb.Text + " - " + Inst_txt.Text;

            List<(string, string, string)> tmp = new List<(string, string, string)>();
            foreach ((string, string, string) t in T_list.Items)
                tmp.Add(t);


            if (idx < Globals.data.Count)
            {
                Globals.data[idx] = new Activity(Name_txt.Text, Inst_txt.Text, Type_cmb.Text, Prereq_cmb.Text, tmp);
                // Overwrite box Settings
                SettingsSave(idx);
                
            }
            else
            {
                Globals.data.Add(new Activity(Name_txt.Text, Inst_txt.Text, Type_cmb.Text, Prereq_cmb.Text, tmp));
                // Save new box Settings
                SettingsSave(-1);
            }

            MessageBox.Show("Success");
            success = true;
            save_pending = false;
        }

        private void Act_list_SelectedIndexChanged(object sender, EventArgs e)
        {
            if (Act_list.SelectedIndex != -1)
            {
                // Load previously saved Settings if you saved it previously
                Settings.Text = "Selected Activity (id = " + Act_list.SelectedIndex + ")";
                SettingsLoad(Act_list.SelectedIndex);
            }
            else
            {
                Settings.Text = "New activity (id = " + Globals.data.Count + ")";
            }
        }


        private void Prereq_cmb_Click(object sender, EventArgs e)
        {
            // Update available data
            List<string> p = new List<string>();
            p.Add("None");
            for (int i = 0; i < Act_list.Items.Count; i++)
            {
                if (i == Act_list.SelectedIndex) continue;
                p.Add(i.ToString() + ": " + Act_list.Items[i]);
            }
            Prereq_cmb.DataSource = p;
        }

        private void T_crs_cmb_Click(object sender, EventArgs e)
        {
            // Update available data
            T_crs_cmb.DataSource = Globals.Courses;
            T_maj_cmb_Click(sender, e);
            T_grp_cmb_Click(sender, e);
        }

        private void T_maj_cmb_Click(object sender, EventArgs e)
        {
            // Update available data
            T_maj_cmb.DataSource = Globals.Majors[T_crs_cmb.SelectedItem.ToString()];
            T_grp_cmb_Click(sender, e);
        }

        private void T_grp_cmb_Click(object sender, EventArgs e)
        {
            // Update available data
            T_grp_cmb.DataSource = Globals.Groups[T_crs_cmb.SelectedItem.ToString() + "-" + T_maj_cmb.SelectedItem.ToString()];
        }
        private void T_add_Click(object sender, EventArgs e)
        {
            // Add target to T_list
            string crs = T_crs_cmb.SelectedItem.ToString();
            string maj = T_maj_cmb.SelectedItem.ToString();
            string grp = T_grp_cmb.SelectedItem.ToString();
            T_list.Items.Add((crs, maj, grp));
        }
        private void T_reset_Click(object sender, EventArgs e)
        {
            // Reset targets list
            T_list.Items.Clear();
        }

        private void Gen_btn_Click(object sender, EventArgs e)
        {
            // Format data[] into input.txt, run python script with input.txt, then open Result.xlsx
            System.IO.File.WriteAllText(@"Input.txt", string.Empty);
            using (System.IO.StreamWriter file = new System.IO.StreamWriter(@"input.txt", true))
            {
                foreach (Activity a in Globals.data)
                {
                    file.WriteLine(1);
                    file.WriteLine(a.a_name);
                    file.WriteLine(a.a_inst);
                    file.WriteLine(a.a_type);
                    file.WriteLine(a.targets.Count);
                    foreach ((string, string, string) t in a.targets)
                    {
                        if (t.Item1 == "All") file.WriteLine("**");
                        else file.WriteLine(t.Item1);

                        if (t.Item2 == "All" && t.Item1 == "B19") file.WriteLine("00");
                        else if (t.Item2 == "All") file.WriteLine("**");
                        else file.WriteLine(t.Item2);

                        if (t.Item3 == "All") file.WriteLine("**");
                        else file.WriteLine(t.Item3);
                    }
                    file.WriteLine(a.refers_to);
                }
                file.WriteLine(5);
                file.WriteLine(string.Empty);
            }
            // MessageBox.Show("Generated Successfully");
            var proc = Process.Start("run.bat");
            proc.WaitForExit();
            Process.Start("Output\\Result.xlsx");
        }

        private void Act_list_Deselect(object sender, MouseEventArgs e)
        {
            // Deselect all items on rightclick
            Name_txt.Text = string.Empty;
            Inst_txt.Text = string.Empty;
            T_list.Items.Clear();
            SetComboBoxesDefaults();
            if (e.Button == MouseButtons.Right && Act_list.SelectedIndex != -1)
                Act_list.SetSelected(Act_list.SelectedIndex, false);
        }
    }
}
