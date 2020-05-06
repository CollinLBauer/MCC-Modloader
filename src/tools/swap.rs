// Are these possible with symbolic linking?
// That would avoid large amounts of unneccesary reads and writes
//  caused by copying files over and over again.
//
// Folder structre and location not yet determined.
// I'm thinking of just having the mod folder match the MCC structure exactly.
// It makes swapping between them much easier,
// Downside is a lot of really small maps are gonna have seemingly pointless nested folders.

fn load_mod(mod_name: &str, ) {
    println!("TODO");
    /* goto modding folder --> mod_name
     * for each subfolder in {halo1\original\buildmaps, halo2\h2_maps_win64_dx11, groundhog\maps, h3?, odst?, h4?, haloreach\maps}
     * - change the link of each file in the game directory to point to the modded 
     * 
     */
}

fn load_vanilla() {
    println!("TODO");
    /* goto modding folder --> _vanilla
     * for every file inside
     * - change the link of each file in the game directory to point to vanilla
     */
}