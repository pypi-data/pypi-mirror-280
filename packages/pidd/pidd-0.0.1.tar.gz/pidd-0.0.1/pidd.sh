#! /usr/bin/env sh

# defaults
[ -n "${PIDD_DNS}" ] || PIDD_DNS="\
9.9.9.9 \
"
[ -n "${PIDD_GIT_CHILD}" ] || PIDD_GIT_CHILD="cd"
[ -n "${PIDD_GIT_PARENT}" ] || PIDD_GIT_PARENT="rwx"

# main
pidd_main () {
    pidd_set_environment_variables
    pidd_set_packages_repositories
    pidd_set_packages_configuration
    #
    pidd_list_working_directory
    pidd_set_https_verification_off
    pidd_set_dns_resolving
    pidd_update_packages_catalog
    pidd_install_packages_tools
    pidd_install_ca_certificates
    pidd_write_ca_certificates
    pidd_update_ca_certificates
    pidd_set_https_verification_on
    pidd_update_packages_catalog
    pidd_upgrade_packages
    pidd_install_git
    pidd_install_python
    # TODO move to Python
    pidd_install_rsync
    # TODO move to Python
    pidd_install_ssh
    pidd_clean_packages_cache
    pidd_install_python_modules
    pidd_write_python_module
    pidd_switch_to_python "${@}"
}

# steps

pidd_set_environment_variables () {
    pidd_step "Set environment variables"
    # set path
    PIDD_PATH="$(realpath "${0}")"
    pidd_echo "PIDD_PATH"
    # set operating system id
    PIDD_OS_ID="$(pidd_grep_os ID)"
    case "${PIDD_OS_ID}" in
        "almalinux") PIDD_OS_ID="${PIDD_OS_ALMA}" ;;
        "alpine") PIDD_OS_ID="${PIDD_OS_ALPINE}" ;;
        "arch") PIDD_OS_ID="${PIDD_OS_ARCH}" ;;
        "debian") PIDD_OS_ID="${PIDD_OS_DEBIAN}" ;;
        "fedora") PIDD_OS_ID="${PIDD_OS_FEDORA}" ;;
        "rocky") PIDD_OS_ID="${PIDD_OS_ROCKY}" ;;
        "ubuntu") PIDD_OS_ID="${PIDD_OS_UBUNTU}" ;;
        *) pidd_error_os "PIDD_OS_ID" ;;
    esac
    # set operating system version
    case "${PIDD_OS_ID}" in
        "${PIDD_OS_ALMA}"|"${PIDD_OS_ARCH}"|"${PIDD_OS_FEDORA}"|"${PIDD_OS_ROCKY}")
            PIDD_OS_VERSION=$(pidd_grep_os VERSION_ID \
                | sed "s|^\([0-9]\+\)\..*|\1|")
        ;;
        "${PIDD_OS_ALPINE}")
            PIDD_OS_VERSION=$(pidd_grep_os VERSION_ID \
                | sed "s|^\([0-9]\+\.[0-9]\+\)\..*|\1|")
        ;;
        "${PIDD_OS_DEBIAN}"|"${PIDD_OS_UBUNTU}")
            PIDD_OS_VERSION="$(pidd_grep_os VERSION_CODENAME)"
        ;;
        *)
    esac
    # check operating system version
    case "${PIDD_OS_ID}" in
        "${PIDD_OS_ALMA}"|"${PIDD_OS_ROCKY}")
            case "${PIDD_OS_VERSION}" in
                "8"|"9") ;;
                *) pidd_error_os "PIDD_OS_VERSION" ;;
            esac
        ;;
        "${PIDD_OS_ALPINE}")
            case "${PIDD_OS_VERSION}" in
                "3.18"|"3.19") ;;
                *) pidd_error_os "PIDD_OS_VERSION" ;;
            esac
        ;;
        "${PIDD_OS_ARCH}")
            case "${PIDD_OS_VERSION}" in
                "20231112"|"20240101") ;;
                *) pidd_error_os "PIDD_OS_VERSION" ;;
            esac
        ;;
        "${PIDD_OS_DEBIAN}")
            case "${PIDD_OS_VERSION}" in
                "bookworm"|"bullseye") ;;
                *) pidd_error_os "PIDD_OS_VERSION" ;;
            esac
        ;;
        "${PIDD_OS_FEDORA}")
            case "${PIDD_OS_VERSION}" in
                "39"|"40") ;;
                *) pidd_error_os "PIDD_OS_VERSION" ;;
            esac
        ;;
        "${PIDD_OS_UBUNTU}")
            case "${PIDD_OS_VERSION}" in
                "jammy"|"noble") ;;
                *) pidd_error_os "PIDD_OS_VERSION" ;;
            esac
        ;;
        *)
    esac
    pidd_split
    pidd_echo "PIDD_OS_ID" "PIDD_OS_VERSION"
    # universal
    PIDD_DNS_FILE="/etc/resolv.conf"
    PIDD_PKG_CA="ca-certificates"
    PIDD_PKG_GIT="git"
    # TODO move to Python
    PIDD_PKG_RSYNC="rsync"
    PIDD_PYTHON_ALIAS="python3"
    pidd_split
    pidd_echo "PIDD_DNS_FILE" "PIDD_PKG_CA" "PIDD_PKG_GIT" "PIDD_PYTHON_ALIAS"
    # set ca command & root
    case "${PIDD_OS_ID}" in
        "${PIDD_OS_ALMA}"|"${PIDD_OS_FEDORA}"|"${PIDD_OS_ROCKY}")
            PIDD_CA_ROOT="/etc/pki/ca-trust/source/anchors"
            PIDD_CMD_CA="update-ca-trust"
        ;;
        "${PIDD_OS_ALPINE}")
            PIDD_CA_ROOT="/usr/local/share/ca-certificates"
            PIDD_CMD_CA="update-ca-certificates"
        ;;
        "${PIDD_OS_ARCH}")
            PIDD_CA_ROOT="/etc/ca-certificates/trust-source/anchors"
            PIDD_CMD_CA="update-ca-trust"
        ;;
        "${PIDD_OS_DEBIAN}"|"${PIDD_OS_UBUNTU}")
            PIDD_CA_ROOT="/usr/local/share/ca-certificates"
            PIDD_CMD_CA="update-ca-certificates"
        ;;
        *)
    esac
    pidd_split
    pidd_echo "PIDD_CA_ROOT" "PIDD_CMD_CA"
    # set package manager
    case "${PIDD_OS_ID}" in
        "${PIDD_OS_ALPINE}")
            PIDD_PM="${PIDD_PM_APK}"
        ;;
        "${PIDD_OS_DEBIAN}"|"${PIDD_OS_UBUNTU}")
            PIDD_PM="${PIDD_PM_APT}"
        ;;
        "${PIDD_OS_ALMA}"|"${PIDD_OS_FEDORA}"|"${PIDD_OS_ROCKY}")
            PIDD_PM="${PIDD_PM_DNF}"
        ;;
        "${PIDD_OS_ARCH}")
            PIDD_PM="${PIDD_PM_PACMAN}"
        ;;
        *)
    esac
    pidd_split
    pidd_echo "PIDD_PM"
    case "${PIDD_PM}" in
        "${PIDD_PM_DNF}")
            PIDD_PM_CLEAN="dnf clean all"
            PIDD_PM_INSTALL="dnf install --assumeyes"
            PIDD_PM_QUERY="rpm --query"
            PIDD_PM_UPDATE="dnf makecache"
            PIDD_PM_UPGRADE="dnf upgrade --assumeyes"
            PIDD_PKG_PKG=""
            PIDD_PM_CONF_PATH="/etc/dnf/dnf.conf"
            PIDD_PM_CONF_TEXT="\
[main]
best=True
clean_requirements_on_remove=True
gpgcheck=1
installonly_limit=3
skip_if_unavailable=False
"
            PIDD_PM_HTTPS_PATH="/etc/dnf/dnf.conf.d/https.conf"
            PIDD_PM_HTTPS_TEXT="\
sslverify=False
"
        ;;
        "${PIDD_PM_APK}")
            PIDD_PM_CLEAN="apk cache purge"
            PIDD_PM_INSTALL="apk add"
            PIDD_PM_QUERY="apk info"
            PIDD_PM_UPDATE="apk update"
            PIDD_PM_UPGRADE="apk upgrade"
            PIDD_PKG_PKG=""
            PIDD_PM_CONF_PATH=""
            PIDD_PM_CONF_TEXT=""
            PIDD_PM_HTTPS_PATH="/etc/apk/repositories.d/https"
            PIDD_PM_HTTPS_TEXT="\
--no-verify
"
        ;;
        "${PIDD_PM_PACMAN}")
            PIDD_PM_CLEAN="pacman --sync --clean --noconfirm"
            PIDD_PM_INSTALL="pacman --sync --noconfirm"
            PIDD_PM_QUERY="pacman --query"
            PIDD_PM_UPDATE="pacman --sync --refresh"
            PIDD_PM_UPGRADE="pacman --sync --sysupgrade --noconfirm"
            PIDD_PKG_PKG=""
            PIDD_PM_CONF_PATH=""
            PIDD_PM_CONF_TEXT=""
            PIDD_PM_HTTPS_PATH="/etc/pacman.d/https.conf"
            PIDD_PM_HTTPS_TEXT="\
SSLVerify = No
"
        ;;
        "${PIDD_PM_APT}")
            PIDD_PM_CLEAN="apt-get clean"
            PIDD_PM_INSTALL="apt-get install --assume-yes"
            PIDD_PM_QUERY="dpkg-query --show"
            PIDD_PM_UPDATE="apt-get update"
            PIDD_PM_UPGRADE="apt-get upgrade --assume-yes"
            PIDD_PKG_PKG="apt-utils"
            PIDD_PM_CONF_PATH="/etc/apt/apt.conf.d/apt.conf"
            PIDD_PM_CONF_TEXT="\
Acquire::Check-Valid-Until True;
APT::Get::Show-Versions True;
APT::Install-Recommends False;
APT::Install-Suggests False;
Dir::Etc::SourceParts \"\";
"
            PIDD_PM_HTTPS_PATH="/etc/apt/apt.conf.d/https"
            PIDD_PM_HTTPS_TEXT="\
Acquire::https::Verify-Peer False;
"
        ;;
        *)
    esac
    pidd_split
    pidd_echo "PIDD_PM_CLEAN" \
        "PIDD_PM_INSTALL" "PIDD_PM_QUERY" "PIDD_PM_UPDATE" "PIDD_PM_UPGRADE"
    pidd_split
    pidd_echo "PIDD_PKG_PKG" "PIDD_PM_CONF_PATH" "PIDD_PM_HTTPS_PATH"
    # specific
    case "${PIDD_OS_ID}" in
        "${PIDD_OS_ALMA}")
            PIDD_URL_DEFAULT="https://repo.almalinux.org/almalinux"
        ;;
        "${PIDD_OS_ALPINE}")
            PIDD_URL_DEFAULT="https://dl-cdn.alpinelinux.org/alpine"
        ;;
        "${PIDD_OS_ARCH}")
            PIDD_URL_DEFAULT="https://geo.mirror.pkgbuild.com"
        ;;
        "${PIDD_OS_DEBIAN}")
            PIDD_URL_DEFAULT="http://deb.debian.org/debian"
        ;;
        "${PIDD_OS_FEDORA}")
            PIDD_URL_DEFAULT="http://download.example/pub/fedora/linux/releases"
        ;;
        "${PIDD_OS_ROCKY}")
            PIDD_URL_DEFAULT="http://dl.rockylinux.org/\$contentdir"
        ;;
        "${PIDD_OS_UBUNTU}")
            PIDD_URL_DEFAULT="http://archive.ubuntu.com/ubuntu"
        ;;
        *)
    esac
    PIDD_URL_CHOSEN="${PIDD_URL_DEFAULT}"
    case "${PIDD_OS_ID}" in
        "${PIDD_OS_ALMA}")
            [ -n "${PIDD_URL_ALMA}" ] && PIDD_URL_CHOSEN="${PIDD_URL_ALMA}"
        ;;
        "${PIDD_OS_ALPINE}")
            [ -n "${PIDD_URL_ALPINE}" ] && PIDD_URL_CHOSEN="${PIDD_URL_ALPINE}"
        ;;
        "${PIDD_OS_ARCH}")
            [ -n "${PIDD_URL_ARCH}" ] && PIDD_URL_CHOSEN="${PIDD_URL_ARCH}"
        ;;
        "${PIDD_OS_DEBIAN}")
            [ -n "${PIDD_URL_DEBIAN}" ] && PIDD_URL_CHOSEN="${PIDD_URL_DEBIAN}" \
            || PIDD_URL_CHOSEN="https://deb.debian.org/debian"
        ;;
        "${PIDD_OS_FEDORA}")
            [ -n "${PIDD_URL_FEDORA}" ] && PIDD_URL_CHOSEN="${PIDD_URL_FEDORA}" \
            || PIDD_URL_CHOSEN="https://rpmfind.net/linux/fedora/linux/releases"
        ;;
        "${PIDD_OS_ROCKY}")
            [ -n "${PIDD_URL_ROCKY}" ] && PIDD_URL_CHOSEN="${PIDD_URL_ROCKY}" \
            || PIDD_URL_CHOSEN="https://dl.rockylinux.org/\$contentdir"
        ;;
        "${PIDD_OS_UBUNTU}")
            [ -n "${PIDD_URL_UBUNTU}" ] && PIDD_URL_CHOSEN="${PIDD_URL_UBUNTU}" \
            || PIDD_URL_CHOSEN="https://ubuntu.mirrors.ovh.net/ubuntu"
        ;;
        *)
    esac
    pidd_split
    pidd_echo "PIDD_URL_DEFAULT" "PIDD_URL_CHOSEN"
    # set python command & package
    case "${PIDD_OS_ID}" in
        "${PIDD_OS_ALMA}"|"${PIDD_OS_ROCKY}")
            PIDD_PYTHON_COMMAND="python3.11"
            PIDD_PYTHON_PACKAGE="python3.11"
        ;;
        "${PIDD_OS_ALPINE}")
            PIDD_PYTHON_COMMAND="python3.11"
            PIDD_PYTHON_PACKAGE="python3"
        ;;
        "${PIDD_OS_ARCH}")
            PIDD_PYTHON_COMMAND="python3.12"
            PIDD_PYTHON_PACKAGE="python"
        ;;
        "${PIDD_OS_DEBIAN}")
            case "${PIDD_OS_VERSION}" in
                "bookworm") PIDD_PYTHON_COMMAND="python3.11" ;;
                "bullseye") PIDD_PYTHON_COMMAND="python3.9" ;;
                *)
            esac
            PIDD_PYTHON_PACKAGE="python3"
        ;;
        "${PIDD_OS_FEDORA}")
            PIDD_PYTHON_COMMAND="python3.12"
            PIDD_PYTHON_PACKAGE="python3"
        ;;
        "${PIDD_OS_UBUNTU}")
            case "${PIDD_OS_VERSION}" in
                "noble") PIDD_PYTHON_COMMAND="python3.12" ;;
                "jammy") PIDD_PYTHON_COMMAND="python3.10" ;;
                *)
            esac
            PIDD_PYTHON_PACKAGE="python3"
        ;;
        *)
    esac
    # set python packages
    case "${PIDD_OS_ID}" in
        "${PIDD_OS_ALMA}"|"${PIDD_OS_FEDORA}"|"${PIDD_OS_ROCKY}")
            PIDD_PYTHON_PACKAGES="/usr/lib64/${PIDD_PYTHON_COMMAND}/site-packages"
        ;;
        "${PIDD_OS_ALPINE}"|"${PIDD_OS_ARCH}")
            PIDD_PYTHON_PACKAGES="/usr/lib/${PIDD_PYTHON_COMMAND}/site-packages"
        ;;
        "${PIDD_OS_DEBIAN}"|"${PIDD_OS_UBUNTU}")
            PIDD_PYTHON_PACKAGES="/usr/lib/${PIDD_PYTHON_ALIAS}/dist-packages"
        ;;
        *)
    esac
    pidd_split
    pidd_echo "PIDD_PYTHON_COMMAND" "PIDD_PYTHON_PACKAGE" "PIDD_PYTHON_PACKAGES"
    # variables
    [ -n "${PIDD_CA_1}" ] && PIDD_CA=true
    # continuous integration platform
    if [ -n "${GITHUB_ACTIONS}" ] ; then
        # github → gitea → forgejo
        if [ -n "${GITHUB_SERVER_URL}" ] ; then
            PIDD_SERVER_URL="${GITHUB_SERVER_URL}"
        else
            pidd_error_ci "GITHUB_SERVER_URL"
        fi
        if [ -n "${GITHUB_REPOSITORY}" ] ; then
            PIDD_PROJECTS_GROUP="$(dirname "${GITHUB_REPOSITORY}")"
            PIDD_PROJECT_NAME="$(basename "${GITHUB_REPOSITORY}")"
        else
            pidd_error_ci "GITHUB_REPOSITORY"
        fi
        if [ -n "${GITHUB_REF_NAME}" ] ; then
            PIDD_PROJECT_BRANCH="${GITHUB_REF_NAME}"
        else
            pidd_error_ci "GITHUB_REF_NAME"
        fi
    elif [ -n "${GITLAB_CI}" ] ; then
        # gitlab
        if [ -n "${CI_SERVER_URL}" ] ; then
            PIDD_SERVER_URL="${CI_SERVER_URL}"
        else
            pidd_error_ci "CI_SERVER_URL"
        fi
        if [ -n "${CI_PROJECT_PATH}" ] ; then
            PIDD_PROJECTS_GROUP="$(dirname "${CI_PROJECT_PATH}")"
            PIDD_PROJECT_NAME="$(basename "${CI_PROJECT_PATH}")"
        else
            pidd_error_ci "CI_PROJECT_PATH"
        fi
        if [ -n "${CI_COMMIT_BRANCH}" ] ; then
            PIDD_PROJECT_BRANCH="${CI_COMMIT_BRANCH}"
        else
            pidd_error_ci "CI_COMMIT_BRANCH"
        fi
    else
        # unsupported
        pidd_error_ci "ø"
    fi
    [ -n "${PIDD_SERVER_URL}" ] || pidd_error_ci "PIDD_SERVER_URL"
    [ -n "${PIDD_PROJECTS_GROUP}" ] || pidd_error_ci "PIDD_PROJECTS_GROUP"
    [ -n "${PIDD_PROJECT_NAME}" ] || pidd_error_ci "PIDD_PROJECT_NAME"
    [ -n "${PIDD_PROJECT_BRANCH}" ] || pidd_error_ci "PIDD_PROJECT_BRANCH"
    #
    PIDD_PROJECTS_URL="${PIDD_SERVER_URL}/${PIDD_PROJECTS_GROUP}"
    #
    pidd_split
    pidd_echo "PIDD_CA"
    pidd_split
    pidd_echo "PIDD_SERVER_URL" \
        "PIDD_PROJECTS_GROUP" "PIDD_PROJECT_NAME" "PIDD_PROJECT_BRANCH"
    pidd_split
    pidd_echo "PIDD_PROJECTS_URL"
    # TODO move to Python
    case "${PIDD_PM}" in
        "${PIDD_PM_APK}"|"${PIDD_PM_APT}") PIDD_PKG_SSH="openssh-client" ;;
        "${PIDD_PM_DNF}") PIDD_PKG_SSH="openssh-clients" ;;
        "${PIDD_PM_PACMAN}") PIDD_PKG_SSH="openssh" ;;
        *)
    esac
}

pidd_set_packages_repositories () {
    pidd_step "Set packages repositories"
    case "${PIDD_OS_ID}" in
        "${PIDD_OS_ALMA}")
            case "${PIDD_OS_VERSION}" in
                "8") \
pidd_set_packages_repositories__file="/etc/yum.repos.d/almalinux.repo" ;;
                "9") \
pidd_set_packages_repositories__file="/etc/yum.repos.d/almalinux-baseos.repo" ;;
                *)
            esac
            pidd_sed "${pidd_set_packages_repositories__file}" \
            "|^mirrorlist|# mirrorlist|" \
            "|${PIDD_URL_DEFAULT}|${PIDD_URL_CHOSEN}|" \
            "|^# baseurl|baseurl|"
        ;;
        "${PIDD_OS_ALPINE}")
            pidd_set_packages_repositories__file="/etc/apk/repositories"
            pidd_write "${pidd_set_packages_repositories__file}" "\
${PIDD_URL_CHOSEN}/v${PIDD_OS_VERSION}/main
${PIDD_URL_CHOSEN}/v${PIDD_OS_VERSION}/community
"
        ;;
        "${PIDD_OS_DEBIAN}")
            pidd_set_packages_repositories__file="/etc/apt/sources.list"
            pidd_write "${pidd_set_packages_repositories__file}" "\
deb ${PIDD_URL_CHOSEN} ${PIDD_OS_VERSION} main
deb ${PIDD_URL_CHOSEN} ${PIDD_OS_VERSION}-backports main
deb ${PIDD_URL_CHOSEN} ${PIDD_OS_VERSION}-updates main
deb ${PIDD_URL_CHOSEN}-security ${PIDD_OS_VERSION}-security main
"
        ;;
        "${PIDD_OS_ROCKY}")
            case "${PIDD_OS_VERSION}" in
                "8") \
pidd_set_packages_repositories__file="/etc/yum.repos.d/Rocky-BaseOS.repo" ;;
                "9") \
pidd_set_packages_repositories__file="/etc/yum.repos.d/rocky.repo" ;;
                *)
            esac
            pidd_sed "${pidd_set_packages_repositories__file}" \
            "|^mirrorlist|# mirrorlist|" \
            "|${PIDD_URL_DEFAULT}|${PIDD_URL_CHOSEN}|" \
            "|^#baseurl|baseurl|"
        ;;
        "${PIDD_OS_UBUNTU}")
            pidd_set_packages_repositories__file="/etc/apt/sources.list"
            pidd_write "${pidd_set_packages_repositories__file}" "\
deb ${PIDD_URL_CHOSEN} ${PIDD_OS_VERSION} main
deb ${PIDD_URL_CHOSEN} ${PIDD_OS_VERSION}-backports main
deb ${PIDD_URL_CHOSEN} ${PIDD_OS_VERSION}-updates main
deb ${PIDD_URL_CHOSEN} ${PIDD_OS_VERSION}-security main
"
        ;;
        *)
    esac
}

pidd_set_packages_configuration () {
    pidd_step "Set packages configuration"
    pidd_write "${PIDD_PM_CONF_PATH}" "${PIDD_PM_CONF_TEXT}"
    case "${PIDD_OS_ID}" in
        "${PIDD_OS_DEBIAN}"|"${PIDD_OS_UBUNTU}")
            export DEBIAN_FRONTEND="noninteractive"
        ;;
        *)
    esac
}

# agnostic steps

pidd_list_working_directory () {
    pidd_step "List working directory"
    pidd_list_working_directory__path="$(realpath .)"
    pidd_ls "${pidd_list_working_directory__path}"
}

pidd_set_https_verification_off () {
    if [ -n "${PIDD_CA}" ] || [ "${PIDD_PM}" = "${PIDD_PM_APT}" ] ; then
        pidd_step "Set HTTPS verification off"
        pidd_mkdir "$(dirname "${PIDD_PM_HTTPS_PATH}")"
        pidd_write "${PIDD_PM_HTTPS_PATH}" "${PIDD_PM_HTTPS_TEXT}"
    fi
}

pidd_set_dns_resolving () {
    pidd_step "Set DNS resolving"
    for pidd_set_dns_resolving__server in ${PIDD_DNS} ; do
        pidd_set_dns_resolving__text="${pidd_set_dns_resolving__text}\
nameserver ${pidd_set_dns_resolving__server}
"
    done
    pidd_write "${PIDD_DNS_FILE}" "${pidd_set_dns_resolving__text}"
}

pidd_update_packages_catalog () {
    pidd_step "Update packages catalog"
    ${PIDD_PM_UPDATE} || exit
}

pidd_install_packages_tools () {
    pidd_step "Install packages tools"
    pidd_install_package "${PIDD_PKG_PKG}"
}

pidd_install_ca_certificates () {
    pidd_step "Install CA"
    pidd_install_package "${PIDD_PKG_CA}"
}

pidd_write_ca_certificates () {
    pidd_step "Write CA certificates"
    pidd_mkdir "${PIDD_CA_ROOT}"
    pidd_write_ca_certificates__index=1
    eval "pidd_write_ca_certificates__text=\
\"\${PIDD_CA_${pidd_write_ca_certificates__index}}\""
    while [ -n "${pidd_write_ca_certificates__text}" ] ; do
        pidd_write_ca_certificates__path="\
${PIDD_CA_ROOT}/${pidd_write_ca_certificates__index}.crt"
        pidd_split
        pidd_write \
        "${pidd_write_ca_certificates__path}" \
        "${pidd_write_ca_certificates__text}"
        pidd_openssl "${pidd_write_ca_certificates__path}"
        pidd_write_ca_certificates__index=$((pidd_write_ca_certificates__index+1))
        eval "pidd_write_ca_certificates__text=\
\"\${PIDD_CA_${pidd_write_ca_certificates__index}}\""
    done
}

pidd_update_ca_certificates () {
    pidd_step "Update CA certificates"
    ${PIDD_CMD_CA} || exit
}

pidd_set_https_verification_on () {
    pidd_step "Set HTTPS verification on"
    pidd_rm "${PIDD_PM_HTTPS_PATH}"
}

pidd_upgrade_packages () {
    pidd_step "Upgrade packages"
    ${PIDD_PM_UPGRADE} || exit
}

pidd_install_git () {
    pidd_step "Install Git"
    pidd_install_package "${PIDD_PKG_GIT}"
}

pidd_install_python () {
    pidd_step "Install Python"
    pidd_install_package "${PIDD_PYTHON_PACKAGE}"
    pidd_split
    pidd_ln_python "${PIDD_PYTHON_COMMAND}"
}

# TODO move to Python
pidd_install_rsync () {
    pidd_step "Install Rsync"
    pidd_install_package "${PIDD_PKG_RSYNC}"
}

# TODO move to Python
pidd_install_ssh () {
    pidd_step "Install SSH"
    pidd_install_package "${PIDD_PKG_SSH}"
}

pidd_clean_packages_cache () {
    pidd_step "Clean packages cache"
    ${PIDD_PM_CLEAN} || exit
}

pidd_install_python_modules () {
    pidd_step "Install Python modules"
    pidd_install_python_modules__root="$(mktemp --directory)" || exit
    echo "→ ${pidd_install_python_modules__root}"
    for pidd_install_python_modules__repository \
    in "${PIDD_GIT_CHILD}" "${PIDD_GIT_PARENT}" ; do
        pidd_split
        pidd_install_python_modules__url="\
${PIDD_PROJECTS_URL}/${pidd_install_python_modules__repository}"
        echo "\
${pidd_install_python_modules__url}
↓"
        git clone \
        "${pidd_install_python_modules__url}" \
        "${pidd_install_python_modules__root}\
/${pidd_install_python_modules__repository}" \
        || exit
        pidd_install_python_modules__path="\
${pidd_install_python_modules__root}\
/${pidd_install_python_modules__repository}\
/${pidd_install_python_modules__repository}"
        echo "\
${pidd_install_python_modules__path}
↓
${PIDD_PYTHON_PACKAGES}"
        cp --recursive \
        "${pidd_install_python_modules__path}" "${PIDD_PYTHON_PACKAGES}" \
        || exit
    done
    pidd_split
    pidd_ls "${PIDD_PYTHON_PACKAGES}"
    pidd_split
    pidd_rm "${pidd_install_python_modules__root}"
}

pidd_write_python_module () {
    pidd_step "Write Python module"
    for pidd_write_python_module__variable \
    in OPEN DOWN VERT SPLT __UP SHUT OS_ID OS_VERSION ; do
        pidd_write_python_module__value="\
$(pidd_echo "PIDD_${pidd_write_python_module__variable}")"
        pidd_write_python_module__text="${pidd_write_python_module__text}\
${pidd_write_python_module__value}
"
    done
    pidd_write "${PIDD_PYTHON_PACKAGES}/env.py" "${pidd_write_python_module__text}\
PIDD_STEP = $((PIDD_STEP+1))
"
}

pidd_switch_to_python () {
    pidd_step "Switch to Python"
    echo "\
${PIDD_PATH}
↓
${PIDD_PYTHON_PACKAGES}/${PIDD_GIT_CHILD}"
    "${PIDD_PYTHON_ALIAS}" -m "${PIDD_GIT_CHILD}" "${@}"
}

# functions

pidd_cat () {
    pidd_cat__file="${1}"
    if [ -n "${pidd_cat__file}" ] ; then
        pidd_open "${pidd_cat__file}"
        cat "${pidd_cat__file}" || exit
        pidd_shut "${pidd_cat__file}"
    fi
}

pidd_echo () {
    if [ -n "${1}" ] ; then
        for pidd_echo__name in "${@}" ; do
            eval "pidd_echo__text=\"\${${pidd_echo__name}}\""
            echo "${pidd_echo__name} = \"${pidd_echo__text}\""
        done
    fi
}

pidd_error_ci () {
    echo "× CI: ${*}"
    exit "${PIDD_ERROR_CI}"
}

pidd_error_os () {
    pidd_error_os__variable="${1}"
    printf "× OS: "
    pidd_echo "${pidd_error_os__variable}"
    exit "${PIDD_ERROR_OS}"
}

pidd_grep_os () {
    pidd_grep_os__variable="${1}"
    if [ -n "${pidd_grep_os__variable}" ] ; then
        grep "^${pidd_grep_os__variable}=" "/etc/os-release" \
        | sed "s|^${pidd_grep_os__variable}=||" \
        | sed "s|^\"\(.*\)\"$|\1|"
    fi
}

pidd_install_package () {
    pidd_install_package__name="${1}"
    if [ -n "${pidd_install_package__name}" ] ; then
        ${PIDD_PM_INSTALL} "${pidd_install_package__name}" || exit
    fi
}

pidd_ln_python () {
    pidd_ln_python__command="${1}"
    if [ -n "${pidd_ln_python__command}" ] ; then
        echo "→ ${PIDD_PYTHON_ALIAS} → ${pidd_ln_python__command}"
        ln -f -s "${pidd_ln_python__command}" "/usr/bin/${PIDD_PYTHON_ALIAS}" \
        || exit
    fi
}

pidd_ls () {
    pidd_ls__path="${1}"
    if [ -n "${pidd_ls__path}" ] ; then
        pidd_open "${pidd_ls__path}"
        ls -a -l "${pidd_ls__path}" || exit
        pidd_shut "${pidd_ls__path}"
    fi
}

pidd_mkdir () {
    pidd_mkdir__path="${1}"
    if [ -n "${pidd_mkdir__path}" ] ; then
        echo "→ ${pidd_mkdir__path}"
        mkdir --parents "${pidd_mkdir__path}" || exit
    fi
}

pidd_open () {
    echo "${PIDD_OPEN}${*}"
}

pidd_openssl () {
    pidd_openssl__file="${1}"
    if [ -f "${pidd_openssl__file}" ] ; then
        openssl x509 \
        -in "${pidd_openssl__file}" \
        -noout -text \
        || exit
    fi
}

pidd_rm () {
    pidd_rm__path="${1}"
    if [ -e "${pidd_rm__path}" ] ; then
        echo "← ${pidd_rm__path}"
        rm -r "${pidd_rm__path}" || exit
    fi
}

pidd_sed () {
    pidd_sed__file="${1}"
    shift
    if [ -f "${pidd_sed__file}" ] ; then
        pidd_cat "${pidd_sed__file}"
        for pidd_sed__regex in "${@}" ; do
            sed --in-place "s${pidd_sed__regex}g" "${pidd_sed__file}" \
            && pidd_cat "${pidd_sed__file}" \
            || exit
        done
    fi
}

pidd_shut () {
    echo "${PIDD_SHUT}${*}"
}

pidd_split () {
    echo "${PIDD_SPLT}"
}

pidd_step () {
    PIDD_STEP=$((PIDD_STEP+1))
    echo "\
${PIDD_DOWN}
${PIDD_VERT} ${PIDD_STEP} ${*}
${PIDD___UP}"
}

pidd_write () {
    pidd_write__file="${1}"
    pidd_write__text="${2}"
    if [ -n "${pidd_write__file}" ] ; then
        [ -f "${pidd_write__file}" ] && pidd_cat "${pidd_write__file}"
        echo "→ ${pidd_write__file}"
        printf "%s" "${pidd_write__text}" > "${pidd_write__file}" || exit
        pidd_cat "${pidd_write__file}"
    fi
}

# constants

PIDD_BOX_DOWN="╭"
PIDD_BOX_LEFT="╴"
PIDD_BOX_RIGHT="╶"
PIDD_BOX_UP="╰"
PIDD_BOX_VERTICAL="│"

PIDD_ERROR_CI=2
PIDD_ERROR_OS=1

PIDD_OS_ALMA="alma"
PIDD_OS_ALPINE="alpine"
PIDD_OS_ARCH="arch"
PIDD_OS_DEBIAN="debian"
PIDD_OS_FEDORA="fedora"
PIDD_OS_ROCKY="rocky"
PIDD_OS_UBUNTU="ubuntu"

PIDD_PM_APK="apk"
PIDD_PM_APT="apt"
PIDD_PM_DNF="dnf"
PIDD_PM_PACMAN="pacman"

PIDD_HORIZONTAL="────╌╌╌╌┄┄┄┄┈┈┈┈"

PIDD_OPEN="${PIDD_BOX_DOWN}${PIDD_BOX_LEFT}"
PIDD_DOWN="${PIDD_BOX_DOWN}${PIDD_HORIZONTAL}"
PIDD_VERT="${PIDD_BOX_VERTICAL}"
PIDD_SPLT="${PIDD_BOX_RIGHT}${PIDD_HORIZONTAL}"
PIDD___UP="${PIDD_BOX_UP}${PIDD_HORIZONTAL}"
PIDD_SHUT="${PIDD_BOX_UP}${PIDD_BOX_LEFT}"

# run
pidd_main "${@}"
