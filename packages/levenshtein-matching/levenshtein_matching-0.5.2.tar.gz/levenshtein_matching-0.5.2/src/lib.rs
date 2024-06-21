use pyo3::{exceptions::PyValueError, prelude::*};
use edit_distance::edit_distance;

#[pyfunction]
/// Calculates the Levenshtein distance between two lists of strings.
/// This function takes a list targets, and queries and performs levenshtein distance operation to find the best matches.
///
/// # Arguments
/// * `target` - A vector of tuples containing strings to be matched for and their associate return value.
/// * `query` - A vector of tuples containing strings to match against target names and their associate return value.
/// * `threshold` - A float value between 0 and 1 that determines the matching threshold. A higher value means a stricter match.
///
/// # Returns
/// A tuple containing two vectors:
/// * A vector of values associated with the first vector of the best matching strings.
/// * A vector of values associated with the second vector of the best matching strings.
///
/// # Errors
/// Returns a `PyValueError` if the threshold is not between 0 and 1.
/// # Example
/// ```python
/// from levenshtein_string_matching import find_best_match_levenshtein
///
/// target = [("String 1", 1), ("String 2", 2)]
/// query = [("String 2", 0.8), ("String 2", 0.5)]
/// threshold = 0.7
///
/// target_values, query_values = find_best_match_levenshtein(target, query, threshold)
/// print(f"Target values: {target_values}")
/// print(f"Query values: {query_values}")
/// ```
fn find_best_match_levenshtein(target: Vec<(String, u64)>, query: Vec<(String, f32)>, threshold: f32) -> PyResult<(Vec<u64>, Vec<f32>)> {
    if threshold < 0.0 || threshold > 1.0 {
        return Err(PyValueError::new_err("threshold must be between 0 and 1"));
    }
    
    let mut valid_matches: (Vec<u64>, Vec<f32>) = (vec![], vec![]);
    for (pa_name, score) in query.iter() {
        let formatted_pa = pa_name.to_lowercase();
        let mut best_match: (usize, String, u64, f32) = (100, "".to_string(), 0, 0.0);
        for (company_name, org_nr ) in target.iter() {
            let formatted_company = company_name.to_lowercase();
            let levenshtein_distance: usize = edit_distance(formatted_pa.trim(), formatted_company.trim());
            if levenshtein_distance == 0 {
                valid_matches.0.push(*org_nr);
                valid_matches.1.push(*score);
                break
            }
            if levenshtein_distance <= best_match.0 {
                best_match = (levenshtein_distance, formatted_company.trim().to_string(), *org_nr, *score);
            }
        }
        if (best_match.0 as f32 / best_match.1.len() as f32) <= 1.0-threshold {
            valid_matches.0.push(best_match.2);
            valid_matches.1.push(best_match.3);
        }
    }
    Ok(valid_matches)
}

/// A Python module implemented in Rust.
#[pymodule]
fn levenshtein_matching(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(find_best_match_levenshtein, m)?)?;
    Ok(())
}

#[test]
fn test_levenshtein() {
    let target = vec![("CAPITAL CASE STRING".to_string(), 1 as u64), ("TYPO STRING".to_string(), 2 as u64)];
    let query = vec![("TYP STRUNG".to_string(), 95.0), ("capital case string".to_string(), 72.0)];
    let (target_values, query_values) = find_best_match_levenshtein(target, query, 0.9).unwrap();

    assert_eq!(target_values.len(), query_values.len());
    assert_eq!(target_values.len(), 1);
    assert_eq!(target_values[0], 1);
}