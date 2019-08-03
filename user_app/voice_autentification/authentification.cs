using System;
using System.Windows.Forms;
using System.Diagnostics;
using System.IO;
using System.Linq;
using System.Text;

namespace voice_autentification
{
    public partial class authentification : Form
    {
        public authentification()
        {
            InitializeComponent();
            
        }
        bool recognized = false;
        bool available_to_play = false;
        private void record_Click(object sender, EventArgs e)
        {
            label3.Text = "Произнесите фразу";
            label2.Text = "Идет запись";
            Process proc1 = new Process();
            proc1.StartInfo.FileName = @"C:\Users\Ралина\PycharmProjects\trial1\verif_record.bat";
            proc1.StartInfo.WorkingDirectory = @"C:\Users\Ралина\PycharmProjects\trial1\";
            proc1.StartInfo.WindowStyle = ProcessWindowStyle.Hidden;
            proc1.Start();
            proc1.WaitForExit();
            label2.Text = File.ReadLines(@"C:\Verification\message.txt", Encoding.Default).First();
            string recogn = File.ReadLines(@"C:\Verification\recognized.txt", Encoding.Default).First();
            if (recogn == "True")
            {
                recognized = true;
                available_to_play = true;
            }
            File.WriteAllText(@"C:\Verification\recognized.txt", String.Empty);
        }

        private void play_Click(object sender, EventArgs e)
        {
            if (available_to_play)
            {
                Process proc1 = new Process();
                proc1.StartInfo.FileName = @"C:\Users\Ралина\PycharmProjects\trial1\demo.bat";
                proc1.StartInfo.WorkingDirectory = @"C:\Users\Ралина\PycharmProjects\trial1\";
                proc1.StartInfo.WindowStyle = ProcessWindowStyle.Hidden;
                proc1.Start();
                proc1.WaitForExit();
            }
            else
                label2.Text = "Нельзя проиграть аудио, так как не была проведена запись либо фраза произнесена неверно.";
        }

        private void recognize_Click(object sender, EventArgs e)
        {
            bool next = false;
            if(recognized)
            {
                Process proc1 = new Process();
                proc1.StartInfo.FileName = @"C:\Users\Ралина\PycharmProjects\trial1\verify.bat";
                proc1.StartInfo.WorkingDirectory = @"C:\Users\Ралина\PycharmProjects\trial1\";
                proc1.StartInfo.WindowStyle = ProcessWindowStyle.Hidden;
                proc1.Start();
                proc1.WaitForExit();
                if (File.ReadLines(@"C:\Verification\verified.txt", Encoding.Default).First() == "True")
                    next = true;
                if (next)
                {
                    password pass = new password();
                    this.Hide();
                    pass.ShowDialog();
                    this.Close();
                }
                else
                    label2.Text = "Вы не были распознаны! Попробуйте записать аудио еще раз.";
            }
            else
                label2.Text = "Запишите аудио!";
            File.WriteAllText(@"C:\Verification\verified.txt", String.Empty);
            
        }

        private void authentification_Load(object sender, EventArgs e)
        {
            label3.Text = "Нажмите кнопку записи, чтобы начать";
            Process proc = new Process();
            proc.StartInfo.FileName = @"C:\Users\Ралина\PycharmProjects\trial1\generate_phrase.bat";
            proc.StartInfo.WorkingDirectory = @"C:\Users\Ралина\PycharmProjects\trial1\";
            proc.StartInfo.WindowStyle = ProcessWindowStyle.Hidden;
            proc.Start();
            proc.WaitForExit();
            label1.Text = File.ReadLines(@"C:\Verification\phrase.txt", Encoding.Default).First();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            Process proc = new Process();
            proc.StartInfo.FileName = @"C:\Users\Ралина\PycharmProjects\trial1\generate_phrase.bat";
            proc.StartInfo.WorkingDirectory = @"C:\Users\Ралина\PycharmProjects\trial1\";
            proc.StartInfo.WindowStyle = ProcessWindowStyle.Hidden;
            proc.Start();
            proc.WaitForExit();
            label1.Text = File.ReadLines(@"C:\Verification\phrase.txt", Encoding.Default).First();
        }
    }
}
