using System;
using System.Windows.Forms;

namespace voice_autentification
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            authentification auth = new authentification();
            this.Hide();
            auth.ShowDialog();
            this.Close();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            registration reg = new registration();
            this.Hide();
            reg.ShowDialog();
            this.Close();
        }
    }
}
