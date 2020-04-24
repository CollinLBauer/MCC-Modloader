// MCC has a modular install.
// This simply checks if each title is installed and returns array of bools.
// Haven't figured out the best way to do this yet.

fn status_sp() -> [&'static bool; 6] {
    // order: {h1, h2, h3, odst, h4, reach}
    let mut sp_status = [false, false, false, false, false, false];

    println!("TODO");

    return sp_status;
}

fn status_mp() -> [&'static bool; 7] {
    // order: {h1, h2, h2a, h3, odst, h4, reach}
    let mut mp_status = [false, false, false, false, false, false];

    println!("TODO");

    return mp_status;
}
