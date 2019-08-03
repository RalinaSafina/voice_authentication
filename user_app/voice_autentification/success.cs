using System;
using System.Windows.Forms;
using System.Diagnostics;
using System.IO;
using System.Linq;
using System.Text;

namespace voice_autentification
{
    public partial class success : Form
    {
        public success()
        {
            InitializeComponent();
        }

        private void success_Load(object sender, EventArgs e)
        {
            label1.Text = "Привет, " + File.ReadLines(@"C:\Verification\name.txt", Encoding.Default).First();
        }
    }
}
