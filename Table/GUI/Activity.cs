using System.Collections.Generic;
using System.Text.RegularExpressions;
using System.Windows.Forms;

namespace ATC_GUI
{
    class Activity
    {
        public string a_name;
        public string a_inst;
        public int a_type;
        public int refers_to;
        public List<(string, string, string)> targets;

        public Activity(string a_name, string a_inst, string a_type, string refers_to, List<(string, string, string)> targets)
        {
            this.a_name = a_name;
            this.a_inst = a_inst;

            if (a_type == "Lecture") this.a_type = 1;
            else if (a_type == "Tutorial") this.a_type = 2;
            else if (a_type == "Lab") this.a_type = 3;

            if (refers_to == "None") this.refers_to = -1;
            else
            {
                string Match = Regex.Match(refers_to, "[0-9]+:").Value;
                this.refers_to = int.Parse(Match.TrimEnd(':'));
            }
            this.targets = targets;
        }
    }
}
