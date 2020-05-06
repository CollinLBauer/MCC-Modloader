// MCC has a modular install.
// This simply checks if each title is installed and returns array of bools.
// Haven't figured out the best way to do this yet.

fn status_sp(mut sp_status: [&'static bool; 6]) {
    // order: {h1, h2, h3, odst, h4, reach}
    sp_status[0] = &false;

    println!("TODO");
}

fn status_mp(mut mp_status: [&'static bool; 7]) {
    // order: {h1, h2, h2a, h3, odst, h4, reach}
    mp_status[0] = &false;

    println!("TODO");
}
