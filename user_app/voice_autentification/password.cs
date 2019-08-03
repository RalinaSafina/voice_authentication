using System;
using System.Windows.Forms;
using System.Diagnostics;
using System.IO;
using System.Linq;
using System.Text;

namespace voice_autentification
{
    public partial class password : Form
    {
        public password()
        {
            InitializeComponent();
        }
        string name = File.ReadLines(@"C:\Verification\name.txt", Encoding.Default).First();

        private void password_Load(object sender, EventArgs e)
        {
            label1.Text = name + ", введите пароль:";
        }

        private void button1_Click(object sender, EventArgs e)
        {
            string password = File.ReadLines(@"C:/Verification/" + name + "/password.txt", Encoding.Default).First();
            if (password == textBox1.Text)
            {
                success success = new success();
                this.Hide();
                success.ShowDialog();
                this.Close();
            }
            else
                label3.Text = "Неверный пароль";
        }

        private void button2_Click(object sender, EventArgs e)
        {
            Form1 form = new Form1();
            this.Hide();
            form.ShowDialog();
            this.Close();
        }
    }
}
