terraform {
  backend "s3" {
    bucket = "lutoskikapu"
    key    = "lutos_terraform.tfstate"
    region = "us-east-1"
    profile = "default"
  }
}
