module "ecr" {
	source = "./modules/ecr"
}
module "eks" {
        source = "./modules/eks"
}
