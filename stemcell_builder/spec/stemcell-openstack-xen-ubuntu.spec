# Setup base chroot
stage base_debootstrap
stage base_apt

# Bosh steps
stage bosh_users
stage bosh_debs
stage bosh_monit
stage bosh_ruby
stage bosh_agent
stage bosh_sysstat
stage bosh_sysctl
stage bosh_ntpdate
stage bosh_sudoers

# Micro BOSH
stage bosh_micro

# Install GRUB/kernel/etc
stage system_grub
stage system_kernel

# Misc
stage system_openstack_network
stage system_openstack_clock
stage system_openstack_modules
stage system_parameters

# Finalisation
stage bosh_clean
stage bosh_harden
stage bosh_harden_ssh
stage bosh_tripwire
stage bosh_dpkg_list

# Image/bootloader
stage image_create
stage image_install_grub
stage image_openstack_update_grub
stage image_openstack_prepare_stemcell

# Final stemcell
stage stemcell_openstack
