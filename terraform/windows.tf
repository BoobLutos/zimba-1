provider "aws" {
  access_key = "AKIACVDUAYMTHHT42265"
  secret_key = "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"
  region     = "us-east-1"
}

resource "aws_instance" "terrawin" {
  ami           = "ami-0193dcf9aa4f5654e"
  instance_type = "t2.micro"
  key_name = "terraformkey1"
  security_groups = ["${aws_security_group.allow_rdp.name}"]

}

resource "aws_security_group" "allow_rdp" {
  name        = "allow_rdp"
  description = "Allow rdp traffic"


  ingress {

    from_port   = 3389 #  By default, the windows server listens on TCP port 3389 for RDP
    to_port     = 3389
    protocol =   "tcp"

    cidr_blocks =  ["0.0.0.0/0"]
  }
}
