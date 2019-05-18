import sys
import subprocess

IP = str(sys.argv[1])
cmd_str = "ping " + IP
subprocess.call(cmd_str, shell=True)

# perl nikto.pl -host 49.212.181.167 -port 38080 -Save "/root/work/Y4Q/02_確認完了/49.212.181.167/_★指摘/nikto_save-38080_49.212.181.167" -Display P -Format txt -output /root/work/Y4Q/02_確認完了/49.212.181.167/_★指摘/nikto_38080-49.212.181.167.txt
# nikto -host 49.212.181.167 -port 38080 -Save "/root/work/Y4Q/02_確認完了/49.212.181.167/_★指摘/nikto_save-38080_49.212.181.167" -Display P -Format txt -output /root/work/Y4Q/02_確認完了/49.212.181.167/_★指摘/nikto_38080-49.212.181.167.txt
