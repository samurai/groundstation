groundstation_dev() {
    requires "libgit2_dev"
    requires "pip_packages_installed"
    process
}

libgit2_dev() {
    function is_met() {
        echo "main() { return 0; }" | gcc -x c /dev/stdin -lgit2 -o /dev/null
    }
    function meet {
        ( [ "`uname -s`" == "Darwin" ] && which brew >/dev/null ) || unmeetable "Only supported on osx"
        brew install --HEAD libgit2
    }
    process
}

virtualenv_exists() {
    #requires "virtualenv installed"
    function is_met() {
        test -d env
    }
    function meet() {
        virtualenv env
    }
    process
}

pip_packages_installed() {
    requires "virtualenv_exists"
    function is_met() {
        (
            . env/bin/activate
            # Nasty
            for i in pygit2 google.protobuf; do
                python -c "import $i" || exit 1
            done
        )
    }
    function meet() {
        (
            . env/bin/activate
            pip install -r requirements.txt
        )
    }
    process
}
