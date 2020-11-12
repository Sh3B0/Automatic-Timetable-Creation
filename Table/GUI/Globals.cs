using System.Collections.Generic;

namespace ATC_GUI
{
    class Globals
    {
        // Data here will be fixed until we generalize the application
        public static List<Activity> data = new List<Activity>();
        public static List<string> Courses = new List<string> { "All", "B17", "B18", "B19", "B20", "M19", "M20" };
        public static Dictionary<string, List<string>> Majors = new Dictionary<string, List<string>>
        {
            { "All", new List<string> {"All"} },
            {"B17", new List<string> {"All", "DS", "SE", "SB", "RO"} },
            {"B18", new List<string> {"All", "DS", "SE", "SB", "RO"} },
            {"B19", new List<string> {"All"} },
            {"B20", new List<string> {"All", "CE", "CS"} },
            {"M19", new List<string> {"All", "SE", "DS", "RO"} },
            {"M20", new List<string> {"All", "RO", "DS"} }

        };

        public static Dictionary<string, List<string>> Groups = new Dictionary<string, List<string>>
        {
            { "All-All", new List<string> {"All"} },
            {"B17-All", new List<string> {"All"} },
            {"B18-All", new List<string> {"All"} },
            {"B20-All", new List<string> {"All"} },
            {"M19-All", new List<string> {"All"} },
            {"M20-All", new List<string> {"All"} },

            {"B17-DS", new List<string> {"All", "01", "02"} },
            {"B17-SE", new List<string> {"All", "01", "02"} },
            {"B17-SB", new List<string> {"All", "01"} },
            {"B17-RO", new List<string> {"All", "01"} },

            {"B18-DS", new List<string> {"All", "01", "02"} },
            {"B18-SE", new List<string> {"All", "01", "02"} },
            {"B18-SB", new List<string> {"All", "01"} },
            {"B19-RO", new List<string> {"All", "01"} },

            {"B19-All", new List<string> {"All", "01", "02", "03", "04", "05", "06"}},

            {"B20-CE", new List<string> {"All", "01", "02", "03", "04"}},
            {"B20-CS", new List<string> {"All", "01", "02"}},

            {"M19-SE", new List<string> {"All", "01"} },
            {"M19-DS", new List<string> {"All", "01"} },
            {"M19-RO", new List<string> {"All", "01"} },

            {"M20-DS", new List<string> {"All", "01"} },
            {"M20-RO", new List<string> {"All", "01"} },
        };

    }
}
