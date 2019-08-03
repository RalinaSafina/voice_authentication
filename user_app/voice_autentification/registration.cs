using System;
using System.Windows.Forms;
using System.Diagnostics;
using System.IO;
using System.Linq;
using System.Text;

namespace voice_autentification
{
    public partial class registration : Form
    {
        public registration()
        {
            InitializeComponent();
        }
        int counter = 0;

        private void registration_Load(object sender, EventArgs e)
        {
            Directory.CreateDirectory(@"C:\Verification\new_user");
            Process proc = new Process();
            proc.StartInfo.FileName = @"C:\Users\Ралина\PycharmProjects\trial1\generate_phrase.bat";
            proc.StartInfo.WorkingDirectory = @"C:\Users\Ралина\PycharmProjects\trial1\";
            proc.StartInfo.WindowStyle = ProcessWindowStyle.Hidden;
            proc.Start();
            proc.WaitForExit();
            string text = File.ReadLines(@"C:\Verification\phrase.txt", Encoding.Default).First();
            label4.Text = text + " (Нормально)";
            label5.Text = text + " (Быстро)";
            label6.Text = text + " (Медленно)";
            label7.Text = text + " (Тихо)";
            label8.Text = text + " (Громко)";
        }

        private void button1_Click(object sender, EventArgs e)
        {
            bool b2 = false, b3 = false, b4 = false, b5 = false;
            button1.Enabled = false;
            if (button2.Enabled)
            {
                button2.Enabled = false;
                b2 = true;
            }
            if (button3.Enabled)
            {
                button3.Enabled = false;
                b3 = true;
            }
            if (button4.Enabled)
            {
                button4.Enabled = false;
                b4 = true;
            }
            if (button5.Enabled)
            {
                button5.Enabled = false;
                b5 = true;
            }
            button6.Enabled = false;
            label9.Visible = true;
            Process proc = new Process();
            proc.StartInfo.FileName = @"C:\Users\Ралина\PycharmProjects\trial1\file1.bat";
            proc.StartInfo.WorkingDirectory = @"C:\Users\Ралина\PycharmProjects\trial1\";
            proc.StartInfo.WindowStyle = ProcessWindowStyle.Hidden;
            proc.Start();
            proc.WaitForExit();
            if(b2)
                button2.Enabled = true;
            if(b3)
                button3.Enabled = true;
            if(b4)
                button4.Enabled = true;
            if(b5)
                button5.Enabled = true;
            button6.Enabled = true;
            counter++;
            label9.Visible = false;
            label14.Visible = true;
        }

        private void button2_Click(object sender, EventArgs e)
        {
            bool b1 = false, b3 = false, b4 = false, b5 = false;
            button2.Enabled = false;
            if (button1.Enabled)
            {
                button1.Enabled = false;
                b1 = true;
            }
            if (button3.Enabled)
            {
                button3.Enabled = false;
                b3 = true;
            }
            if (button4.Enabled)
            {
                button4.Enabled = false;
                b4 = true;
            }
            if (button5.Enabled)
            {
                button5.Enabled = false;
                b5 = true;
            }
            button6.Enabled = false;
            label10.Visible = true;
            Process proc = new Process();
            proc.StartInfo.FileName = @"C:\Users\Ралина\PycharmProjects\trial1\file2.bat";
            proc.StartInfo.WorkingDirectory = @"C:\Users\Ралина\PycharmProjects\trial1\";
            proc.StartInfo.WindowStyle = ProcessWindowStyle.Hidden;
            proc.Start();
            proc.WaitForExit();
            if (b1)
                button1.Enabled = true;
            if (b3)
                button3.Enabled = true;
            if (b4)
                button4.Enabled = true;
            if (b5)
                button5.Enabled = true;
            button6.Enabled = true;
            counter++;
            label10.Visible = false;
            label15.Visible = true;
        }

        private void button3_Click(object sender, EventArgs e)
        {
            bool b2 = false, b1 = false, b4 = false, b5 = false;
            button3.Enabled = false;
            if (button2.Enabled)
            {
                button2.Enabled = false;
                b2 = true;
            }
            if (button1.Enabled)
            {
                button1.Enabled = false;
                b1 = true;
            }
            if (button4.Enabled)
            {
                button4.Enabled = false;
                b4 = true;
            }
            if (button5.Enabled)
            {
                button5.Enabled = false;
                b5 = true;
            }
            button6.Enabled = false;
            label11.Visible = true;
            Process proc = new Process();
            proc.StartInfo.FileName = @"C:\Users\Ралина\PycharmProjects\trial1\file3.bat";
            proc.StartInfo.WorkingDirectory = @"C:\Users\Ралина\PycharmProjects\trial1\";
            proc.StartInfo.WindowStyle = ProcessWindowStyle.Hidden;
            proc.Start();
            proc.WaitForExit();
            if (b2)
                button2.Enabled = true;
            if (b1)
                button1.Enabled = true;
            if (b4)
                button4.Enabled = true;
            if (b5)
                button5.Enabled = true;
            button6.Enabled = true;
            counter++;
            label11.Visible = false;
            label16.Visible = true;
        }

        private void button4_Click(object sender, EventArgs e)
        {
            bool b2 = false, b3 = false, b1 = false, b5 = false;
            button4.Enabled = false;
            if (button2.Enabled)
            {
                button2.Enabled = false;
                b2 = true;
            }
            if (button3.Enabled)
            {
                button3.Enabled = false;
                b3 = true;
            }
            if (button1.Enabled)
            {
                button1.Enabled = false;
                b1 = true;
            }
            if (button5.Enabled)
            {
                button5.Enabled = false;
                b5 = true;
            }
            button6.Enabled = false;
            label12.Visible = true;
            Process proc = new Process();
            proc.StartInfo.FileName = @"C:\Users\Ралина\PycharmProjects\trial1\file4.bat";
            proc.StartInfo.WorkingDirectory = @"C:\Users\Ралина\PycharmProjects\trial1\";
            proc.StartInfo.WindowStyle = ProcessWindowStyle.Hidden;
            proc.Start();
            proc.WaitForExit();
            if (b2)
                button2.Enabled = true;
            if (b3)
                button3.Enabled = true;
            if (b1)
                button1.Enabled = true;
            if (b5)
                button5.Enabled = true;
            button6.Enabled = true;
            counter++;
            label12.Visible = false;
            label17.Visible = true;
        }

        private void button5_Click(object sender, EventArgs e)
        {
            bool b2 = false, b3 = false, b4 = false, b1 = false;
            button5.Enabled = false;
            if (button2.Enabled)
            {
                button2.Enabled = false;
                b2 = true;
            }
            if (button3.Enabled)
            {
                button3.Enabled = false;
                b3 = true;
            }
            if (button4.Enabled)
            {
                button4.Enabled = false;
                b4 = true;
            }
            if (button1.Enabled)
            {
                button1.Enabled = false;
                b1 = true;
            }
            button6.Enabled = false;
            label13.Visible = true;
            Process proc = new Process();
            proc.StartInfo.FileName = @"C:\Users\Ралина\PycharmProjects\trial1\file5.bat";
            proc.StartInfo.WorkingDirectory = @"C:\Users\Ралина\PycharmProjects\trial1\";
            proc.StartInfo.WindowStyle = ProcessWindowStyle.Hidden;
            proc.Start();
            proc.WaitForExit();
            if (b2)
                button2.Enabled = true;
            if (b3)
                button3.Enabled = true;
            if (b4)
                button4.Enabled = true;
            if (b1)
                button1.Enabled = true;
            button6.Enabled = true;
            counter++;
            label13.Visible = false;
            label18.Visible = true;
        }

        private void button6_Click(object sender, EventArgs e)
        {
            if(counter == 5 && textBox1.Text != "" && textBox2.Text != "")
            {
                Process proc = new Process();
                proc.StartInfo.FileName = @"C:\Users\Ралина\PycharmProjects\trial1\etalon_matrix.bat";
                proc.StartInfo.WorkingDirectory = @"C:\Users\Ралина\PycharmProjects\trial1\";
                proc.StartInfo.WindowStyle = ProcessWindowStyle.Hidden;
                proc.Start();
                proc.WaitForExit();
                FileStream filestream = new FileStream(@"C:\Verification\new_user\password.txt", FileMode.Create);
                StreamWriter streamwriter = new StreamWriter(filestream);
                streamwriter.Write(textBox2.Text);
                streamwriter.Flush();
                streamwriter.Close();
                filestream.Close();
                Directory.Move(@"C:\Verification\new_user", @"C:\Verification\" + textBox1.Text);
                Form1 form = new Form1();
                this.Hide();
                form.ShowDialog();
                this.Close();
            }
            else
            {
                MessageBox.Show("Проверьте наличие данных и записей голоса.");
            }
        }
    }
}
