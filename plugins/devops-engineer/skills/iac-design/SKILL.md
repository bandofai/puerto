# Infrastructure as Code Design Skill

**Expert-level IaC patterns for Terraform, CloudFormation, and multi-cloud infrastructure**

## Core Principles

1. **Immutable Infrastructure**: Replace, don't modify
2. **DRY (Don't Repeat Yourself)**: Use modules and composition
3. **State Management**: Remote state with locking
4. **Security First**: Least privilege, encryption, audit
5. **Cost Awareness**: Tag everything, right-size resources

## Module Design Pattern

```
terraform/
├── modules/              # Reusable components
│   ├── vpc/
│   │   ├── main.tf
│   │   ├── variables.tf
│   │   ├── outputs.tf
│   │   └── README.md
│   ├── compute/
│   ├── database/
│   └── monitoring/
├── environments/         # Environment-specific configs
│   ├── dev/
│   │   ├── main.tf
│   │   ├── variables.tf
│   │   ├── terraform.tfvars
│   │   └── backend.tf
│   ├── staging/
│   └── prod/
└── README.md
```

### Module Best Practices
- **Single Responsibility**: One module = one logical component
- **Versioned**: Tag modules with semantic versions
- **Documented**: README with examples
- **Validated**: Input validation with `validation` blocks
- **Tested**: Use Terratest or similar

## Terraform Patterns

### Variable Validation
```hcl
variable "environment" {
  type        = string
  description = "Environment name"
  validation {
    condition     = contains(["dev", "staging", "prod"], var.environment)
    error_message = "Environment must be dev, staging, or prod."
  }
}

variable "instance_type" {
  type        = string
  description = "EC2 instance type"
  validation {
    condition     = can(regex("^t3\\.(micro|small|medium|large|xlarge)$", var.instance_type))
    error_message = "Instance type must be a valid t3 instance."
  }
}
```

### Dynamic Blocks
```hcl
resource "aws_security_group" "app" {
  name = "${var.environment}-app-sg"

  dynamic "ingress" {
    for_each = var.ingress_rules
    content {
      from_port   = ingress.value.port
      to_port     = ingress.value.port
      protocol    = "tcp"
      cidr_blocks = ingress.value.cidr_blocks
    }
  }
}
```

### Conditional Resources
```hcl
resource "aws_instance" "bastion" {
  count = var.enable_bastion ? 1 : 0

  ami           = data.aws_ami.ubuntu.id
  instance_type = "t3.micro"
  subnet_id     = module.vpc.public_subnets[0]
}
```

### For_Each Pattern
```hcl
locals {
  subnets = {
    public-1  = { cidr = "10.0.1.0/24", az = "us-east-1a" }
    public-2  = { cidr = "10.0.2.0/24", az = "us-east-1b" }
    private-1 = { cidr = "10.0.10.0/24", az = "us-east-1a" }
    private-2 = { cidr = "10.0.11.0/24", az = "us-east-1b" }
  }
}

resource "aws_subnet" "subnets" {
  for_each = local.subnets

  vpc_id            = aws_vpc.main.id
  cidr_block        = each.value.cidr
  availability_zone = each.value.az

  tags = {
    Name = "${var.environment}-${each.key}"
  }
}
```

## State Management

### Remote State (S3 Backend)
```hcl
terraform {
  backend "s3" {
    bucket         = "my-terraform-state"
    key            = "prod/terraform.tfstate"
    region         = "us-east-1"
    encrypt        = true
    dynamodb_table = "terraform-state-lock"
    kms_key_id     = "arn:aws:kms:us-east-1:123456789:key/abc-def"
  }
}
```

### State Locking (DynamoDB)
```hcl
resource "aws_dynamodb_table" "terraform_state_lock" {
  name           = "terraform-state-lock"
  billing_mode   = "PAY_PER_REQUEST"
  hash_key       = "LockID"

  attribute {
    name = "LockID"
    type = "S"
  }

  tags = {
    Name    = "Terraform State Lock Table"
    Purpose = "State locking"
  }
}
```

### Workspace Strategy
```bash
# Create workspaces for environments
terraform workspace new dev
terraform workspace new staging
terraform workspace new prod

# Switch workspace
terraform workspace select prod

# Use workspace in config
resource "aws_instance" "app" {
  tags = {
    Environment = terraform.workspace
  }
}
```

## Security Patterns

### IAM Least Privilege
```hcl
resource "aws_iam_role_policy" "app" {
  name = "${var.environment}-app-policy"
  role = aws_iam_role.app.id

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect = "Allow"
        Action = [
          "s3:GetObject",
          "s3:PutObject"
        ]
        Resource = "${aws_s3_bucket.app.arn}/*"
      },
      {
        Effect = "Allow"
        Action = [
          "dynamodb:GetItem",
          "dynamodb:PutItem",
          "dynamodb:UpdateItem"
        ]
        Resource = aws_dynamodb_table.app.arn
      }
    ]
  })
}
```

### Encryption at Rest
```hcl
# RDS with encryption
resource "aws_db_instance" "app" {
  storage_encrypted = true
  kms_key_id        = aws_kms_key.rds.arn
}

# S3 with encryption
resource "aws_s3_bucket" "app" {
  bucket = "${var.environment}-app-data"
}

resource "aws_s3_bucket_server_side_encryption_configuration" "app" {
  bucket = aws_s3_bucket.app.id

  rule {
    apply_server_side_encryption_by_default {
      sse_algorithm     = "aws:kms"
      kms_master_key_id = aws_kms_key.s3.arn
    }
  }
}

# EBS with encryption
resource "aws_ebs_volume" "app" {
  encrypted  = true
  kms_key_id = aws_kms_key.ebs.arn
}
```

### Network Isolation
```hcl
# Private subnets for sensitive resources
resource "aws_subnet" "private" {
  for_each = local.private_subnets

  vpc_id            = aws_vpc.main.id
  cidr_block        = each.value.cidr
  availability_zone = each.value.az

  tags = {
    Name = "${var.environment}-private-${each.key}"
    Tier = "private"
  }
}

# Security group with minimal access
resource "aws_security_group" "database" {
  name   = "${var.environment}-database-sg"
  vpc_id = aws_vpc.main.id

  ingress {
    from_port       = 5432
    to_port         = 5432
    protocol        = "tcp"
    security_groups = [aws_security_group.app.id]  # Only from app tier
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}
```

### Secrets Management
```hcl
# Store secrets in AWS Secrets Manager
resource "aws_secretsmanager_secret" "db_password" {
  name = "${var.environment}-db-password"
  kms_key_id = aws_kms_key.secrets.id
}

resource "aws_secretsmanager_secret_version" "db_password" {
  secret_id     = aws_secretsmanager_secret.db_password.id
  secret_string = random_password.db_password.result
}

# Reference in RDS
resource "aws_db_instance" "app" {
  password = aws_secretsmanager_secret_version.db_password.secret_string
}
```

## High Availability Patterns

### Multi-AZ Deployment
```hcl
# Distribute across availability zones
locals {
  azs = ["us-east-1a", "us-east-1b", "us-east-1c"]
}

resource "aws_subnet" "public" {
  count             = length(local.azs)
  vpc_id            = aws_vpc.main.id
  cidr_block        = cidrsubnet(var.vpc_cidr, 8, count.index)
  availability_zone = local.azs[count.index]
}

# RDS Multi-AZ
resource "aws_db_instance" "app" {
  multi_az = true  # Automatic failover
}

# ELB across AZs
resource "aws_lb" "app" {
  subnets = aws_subnet.public[*].id  # All AZs
}
```

### Auto Scaling
```hcl
resource "aws_autoscaling_group" "app" {
  name                = "${var.environment}-app-asg"
  vpc_zone_identifier = aws_subnet.private[*].id
  min_size            = var.asg_min_size
  max_size            = var.asg_max_size
  desired_capacity    = var.asg_desired_capacity
  health_check_type   = "ELB"
  health_check_grace_period = 300

  launch_template {
    id      = aws_launch_template.app.id
    version = "$Latest"
  }

  tag {
    key                 = "Name"
    value               = "${var.environment}-app"
    propagate_at_launch = true
  }
}

resource "aws_autoscaling_policy" "scale_up" {
  name                   = "${var.environment}-scale-up"
  autoscaling_group_name = aws_autoscaling_group.app.name
  adjustment_type        = "ChangeInCapacity"
  scaling_adjustment     = 1
  cooldown               = 300
}

resource "aws_cloudwatch_metric_alarm" "cpu_high" {
  alarm_name          = "${var.environment}-cpu-high"
  comparison_operator = "GreaterThanThreshold"
  evaluation_periods  = "2"
  metric_name         = "CPUUtilization"
  namespace           = "AWS/EC2"
  period              = "120"
  statistic           = "Average"
  threshold           = "70"

  dimensions = {
    AutoScalingGroupName = aws_autoscaling_group.app.name
  }

  alarm_actions = [aws_autoscaling_policy.scale_up.arn]
}
```

## Cost Optimization

### Resource Tagging
```hcl
# Standard tags module
locals {
  standard_tags = {
    Environment = var.environment
    Project     = var.project_name
    ManagedBy   = "Terraform"
    Owner       = var.owner_email
    CostCenter  = var.cost_center
  }
}

resource "aws_instance" "app" {
  tags = merge(
    local.standard_tags,
    {
      Name = "${var.environment}-app-server"
      Role = "application"
    }
  )
}
```

### Instance Right-Sizing
```hcl
# Use appropriate instance types per environment
locals {
  instance_types = {
    dev     = "t3.micro"    # $0.0104/hour
    staging = "t3.small"    # $0.0208/hour
    prod    = "t3.medium"   # $0.0416/hour
  }
}

resource "aws_instance" "app" {
  instance_type = local.instance_types[var.environment]
}
```

### Scheduled Scaling (Non-Prod)
```hcl
# Scale down non-prod at night
resource "aws_autoscaling_schedule" "scale_down" {
  count = var.environment != "prod" ? 1 : 0

  scheduled_action_name  = "scale-down"
  min_size               = 0
  max_size               = 0
  desired_capacity       = 0
  recurrence             = "0 22 * * MON-FRI"  # 10 PM weekdays
  autoscaling_group_name = aws_autoscaling_group.app.name
}

resource "aws_autoscaling_schedule" "scale_up" {
  count = var.environment != "prod" ? 1 : 0

  scheduled_action_name  = "scale-up"
  min_size               = var.asg_min_size
  max_size               = var.asg_max_size
  desired_capacity       = var.asg_desired_capacity
  recurrence             = "0 8 * * MON-FRI"  # 8 AM weekdays
  autoscaling_group_name = aws_autoscaling_group.app.name
}
```

## Data Sources

### Reuse Existing Resources
```hcl
# Use existing VPC
data "aws_vpc" "existing" {
  filter {
    name   = "tag:Name"
    values = ["${var.environment}-vpc"]
  }
}

# Latest AMI
data "aws_ami" "ubuntu" {
  most_recent = true
  owners      = ["099720109477"]  # Canonical

  filter {
    name   = "name"
    values = ["ubuntu/images/hvm-ssd/ubuntu-jammy-22.04-amd64-server-*"]
  }
}

# Current AWS region
data "aws_region" "current" {}

# Current AWS account
data "aws_caller_identity" "current" {}
```

## CloudFormation Patterns

### Stack Parameters
```yaml
Parameters:
  EnvironmentName:
    Type: String
    AllowedValues:
      - dev
      - staging
      - prod
    Default: dev

  InstanceType:
    Type: String
    Default: t3.medium
    AllowedValues:
      - t3.micro
      - t3.small
      - t3.medium
      - t3.large

Mappings:
  EnvironmentConfig:
    dev:
      MinSize: 1
      MaxSize: 2
    staging:
      MinSize: 2
      MaxSize: 4
    prod:
      MinSize: 3
      MaxSize: 10
```

### Cross-Stack References
```yaml
# Network stack exports
Outputs:
  VpcId:
    Value: !Ref VPC
    Export:
      Name: !Sub ${EnvironmentName}-VpcId

  PrivateSubnets:
    Value: !Join [",", [!Ref PrivateSubnet1, !Ref PrivateSubnet2]]
    Export:
      Name: !Sub ${EnvironmentName}-PrivateSubnets

# Application stack imports
Resources:
  AppSecurityGroup:
    Type: AWS::EC2::SecurityGroup
    Properties:
      VpcId: !ImportValue
        Fn::Sub: ${EnvironmentName}-VpcId
```

## Troubleshooting

### Terraform State Issues
```bash
# State is locked
terraform force-unlock <lock-id>

# Refresh state
terraform refresh

# Import existing resource
terraform import aws_instance.app i-1234567890abcdef0

# Remove from state (doesn't delete resource)
terraform state rm aws_instance.app

# Move resource in state
terraform state mv aws_instance.old aws_instance.new
```

### Terraform Plan Failures
```bash
# Validate syntax
terraform validate

# Format files
terraform fmt -recursive

# Show detailed plan
terraform plan -out=tfplan
terraform show tfplan
```

## Best Practices Summary

✅ **DO**:
- Use remote state with locking
- Implement least privilege IAM
- Encrypt everything (rest + transit)
- Tag all resources
- Use modules for reusability
- Validate inputs
- Version control everything
- Document modules
- Implement blast radius limits
- Use workspaces or separate states per environment

❌ **DON'T**:
- Hardcode secrets
- Use default VPC/subnets
- Grant `*` permissions
- Skip encryption
- Use root account
- Manually modify infrastructure
- Share state files insecurely
- Skip cost tagging
- Deploy untested changes to prod
- Use latest AMI/image without pinning

---

**Version**: 1.0.0
**Patterns**: Production-tested across AWS, Azure, GCP
